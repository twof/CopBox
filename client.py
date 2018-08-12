import socket
import json

def send_file_to_port(port, name, data):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(('0.0.0.0', port))
  client.setblocking(0)
  client.send(json.dumps({ 'name': name, 'data': data }))
  client.close()

send_file_to_port(5000, 'hey', 'heyy')