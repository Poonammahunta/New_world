import socket, sys

HOST = ''
PORT = 7777

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "socket created"

# To bind socket with host and port
try:
    s.bind(HOST,PORT)
except:
    print "Bind Failed"

print "socket bind completed"

#To start listen on socket
 
s.listen(5)
print "socket is listening"

conn, addr = s.accept()
print ('connected by',addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)

conn.close()

    
