import select, socket, sys, json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen(10)
inputs = [server]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            inputs.append(connection)
            message_queues[connection] = ''
            print("Connection Received:" + str(connection.getpeername()))
        else:
            data = s.recv(1024)
            if data:
                message_queues[s] += data
            else:
                inputs.remove(s)
                meta = json.loads(message_queues[s])
                f = open(meta['name'], 'wb')
                f.write(meta['data'])
                f.close()
                print("Server received file.")
                del message_queues[s]
    for s in writable:
        s.close()
        outputs.remove(s)
    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]

