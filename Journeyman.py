import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 50000

sock.bind((host, port))

sock.listen(1)

conn, addr = sock.accept()

conn.recv(1024)

sock.close()
conn.close()