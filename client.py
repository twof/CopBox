import socket
import json

def send_file(host, port, name, data):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))
  client.setblocking(0)
  client.send(json.dumps({ 'name': name, 'data': data }))
  client.close()
