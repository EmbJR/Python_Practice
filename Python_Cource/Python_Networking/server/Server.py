import socket
host = "127.0.0.1"
port = 5001
server = socket.socket()
server.bind((host, port))
server.listen()
conn, addr = server.accept()
data = conn.recv(1024).decode()
filename='master_m3u8-02.mp4'
f = open(filename,'rb')
while True:
    l = f.read(1024)
    if not l:
        break
    conn.send(l)
    print('Sent ',repr(l))
f.close()
print('File transferred')
conn.close()