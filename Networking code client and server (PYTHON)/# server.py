# server

import socket

s = socket.socket()
host = socket.gethostname()
port = 6666

try:
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    message = conn.recv(1024).decode()
    print('Client Says =', message)
    conn.close()
except Exception as e:
    print(e)
