# client

import socket

s = socket.socket()
host = '192.168.1.37'
port = 6666

try:
    s.connect((host, port))
    message = 'Hello Server'
    s.send(message.encode())
    s.close()
except Exception as e:
    print(e)
