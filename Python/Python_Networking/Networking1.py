'''-------------------------------- Python - Network Programming ----------------------------
The threading module in Python's standard library is capable of handling multiple threads
and their interaction within a single process. Communication between two processes
running on the same machine is handled by Unix domain sockets, whereas for the
processes running on different machines connected with TCP (Transmission control
protocol), Internet domain sockets are used.

Python's standard library consists of various built-in modules that support interprocess
communication and networking. Python provides two levels of access to the network
services. At a low level, you can access the basic socket support in the underlying
operating system, which allows you to implement clients and servers for both connection-
oriented and connectionless protocols.

Python also has libraries that provide higher-level access to specific application-level
network protocols, such as FTP, HTTP, and so on.

| Protocol | Common function        | Port No | Python module(s)                               |
| :------- | :--------------------- | :------ | :--------------------------------------------- |
| HTTP     | Web pages              | 80      | `httplib`, `urllib`, `xmlrpclib`               |
| NNTP     | Usenet news            | 119     | `nntplib`                                      |
| FTP      | File transfers         | 20      | `ftplib`, `urllib`                             |
| SMTP     | Sending email          | 25      | `smtplib`                                      |
| POP3     | Fetching email         | 110     | `poplib`                                       |
| IMAP4    | Fetching email         | 143     | `imaplib`                                      |
| Telnet   | Command lines          | 23      | `telnetlib`                                    |
| Gopher   | Document transfers     | 70      | `gopherlib`, `urllib`                          |

'''

'''----------------------------- Python - Socket Programming ---------------------------
Python Socket Programming
Socket programming is a technique in which we communicate between two nodes
connected in a network where the server node listens to the incoming requests from the
client nodes.

In Python, the socket module is used for socket programming. The socket module in the
standard library included functionality required for communication between server and
client at hardware level.

This module provides access to the BSD socket interface. It is available on all operating
systems such as Linux, Windows, MacOS.'''

''' What are Sockets?
Sockets are the endpoints of a bidirectional communications channel. Sockets may
communicate within a process, between processes on the same machine, or between
processes on different machines.

A socket is identified by the combination of IP address and the port number. It should be
properly configured at both ends to begin communication.

Sockets may be implemented over a number of different channel types: Unix domain
sockets, TCP, UDP, and so on. The socket library provides specific classes for handling the
common transports as well as a generic interface for handling the rest.

The term socket programming implies programmatically setting up sockets to be able to
send and receive data.

There are two types of communication protocols −
     connection-oriented protocol
     connection-less protocol
TCP or Transmission Control Protocol is a connection-oriented protocol. The data is
transmitted in packets by the server, and assembled in the same order of transmission by
the receiver. Since the sockets at either end of the communication need to be set before
starting, this method is more reliable.

UDP or User Datagram Protocol is connectionless. The method is not reliable because the
sockets does not require establishing any connection and termination process for
transferring the data.'''

''' Python socket Module
The socket module is used for creating and managing socket programming for the
connected nodes in a network. The socket module provides a socket class. You need to
create a socket using the socket.socket() constructor.

An object of the socket class represents the pair of host name and the port numbers.

Syntax:- socket.socket (socket_family, socket_type, protocol=0)

Parameters
     family − AF_INET by default. Other values - AF_INET6 (eight groups of four
        hexadecimal digits), AF_UNIX, AF_CAN (Controller Area Network) or AF_RDS
        (Reliable Datagram Sockets).
     socket_type − should be SOCK_STREAM (the default), SOCK_DGRAM,
        SOCK_RAW or perhaps one of the other SOCK_ constants.
     protocol − number is usually zero and may be omitted.

Return Type
This method returns a socket object.
Once you have the socket object, then you can use the required methods to create your
client or server program.'''


''' Server Socket Methods
The socket instantiated on server is called server socket. Following methods are available
to the socket object on the server −
     bind() method − This method binds the socket to specified IP address and port
    number.
     listen() method − This method starts server and runs into a listen loop looking
    for connection request from client.
     accept() method − When connection request is intercepted by server, this
        method accepts it and identifies the client socket with its address.

To create a socket on a server, use the following snippe'''

import socket
server = socket.socket()
server.bind(('localhost',12345))
server.listen()
client, addr = server.accept()
print ("connection request from: " + str(addr))
server.close()  # if you want to close the connection.

''' Client Socket Methods
Similar socket is set up on the client end. It mainly sends connection request to server
socket listening at its IP address and port number

<connect() method>
This method takes a two-item tuple object as argument. The two items are IP address and
port number of the server.
------------------
obj=socket.socket()
obj.connect((host,port))
------------------
Once the connection is accepted by the server, both the socket objects can send and/or
receive data.'''

''' 
<send() method>
The server sends data to client by using the address it has intercepted.
client.send(bytes)
Client socket sends data to socket it has established connection with the server socket.

<sendall() method>
Similar to send(). However, unlike send(),this method continues to send data from bytes
until either all data has been sent or an error occurs. None is returned on success.

<sendto() method>
This method is to be used in case of UDP protocol only.

<recv() method>
This method is used to retrieve data sent to the client. In case of server, it uses the remote
socket whose request has been accepted.
    client.recv(bytes)
    
<recvfrom() method>
This method is used in case of UDP protocol.'''

''' Python - Socket Server
To write Internet servers, we use the socket function available in socket module to create
a socket object. A socket object is then used to call other functions to setup a socket
server.

Now call the bind(hostname, port) function to specify a port for your service on the given
host.

Next, call the accept method of the returned object. This method waits until a client
connects to the port you specified, and then returns a connection object that represents
the connection to that client.
Example of Server Socket'''

import socket
#host = "127.0.0.1"
host = socket.gethostbyname(socket.gethostname())

port = 5001
server = socket.socket()
server.bind((host,port))
server.listen()
conn, addr = server.accept()
print ("Connection from: " + str(addr))
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    data = str(data).upper()
    print (" from client: " + str(data))
    data = input("type message: ")
    conn.send(data.encode())
conn.close()

''' Python - Socket Client
Let us write a very simple client program, which opens a connection to a given port 5001
and a given localhost. It is very simple to create a socket client using the Python's socket
module function.

The socket.connect(hosname, port) opens a TCP connection to hostname on the port. Once
you have a socket open, you can read from it like any IO object. When done, remember
to close it, as you would close a file.

Example of Client Socket
The following code is a very simple client that connects to a given host and port, reads
any available data from the socket, and then exits when 'q' is entered.'''

import socket
host = '10.122.189.109'
port = 5001
obj = socket.socket()
obj.connect((host,port))
message = input("type message: ")
while message != 'q':
    obj.send(message.encode())
    data = obj.recv(1024).decode()
    print ('Received from server: ' + data)
    message = input("type message: ")
obj.close()

'''Python File Transfer with Socket Module
The following program demonstrates how socket communication can be used to transfer
a file from server to the client

Server Code
The code for establishing connection is same as before. After the connection request is
accepted, a file on server is opened in binary mode for reading, and bytes are successively
read and sent to the client stream till end of file is reached.'''

import socket
host = "127.0.0.1"
port = 5001
server = socket.socket()
server.bind((host, port))
server.listen()
conn, addr = server.accept()
data = conn.recv(1024).decode()
filename='test.txt'
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


''' Client Code
On the client side, a new file is opened in wb mode. The stream of data received from
server is written to the file. As the stream ends, the output file is closed. A new file will be
created on the client machine.'''

import socket
s = socket.socket()
host = "127.0.0.1"
port = 5001
s.connect((host, port))
s.send("Hello server!".encode())
with open('recv.txt', 'wb') as f:
    while True:
        print('receiving data...')
        data = s.recv(1024)
        if not data:
            break
        f.write(data)
f.close()
print('Successfully received')
s.close()
print('connection closed')


''' The Python socketserver Module
The socketserver module in Python's standard library is a framework for simplifying task
of writing network servers. There are following classes in module, which represent
synchronous servers. These classes work with corresponding RequestHandler classes for implementing the
service. 

1> BaseServer is the superclass of all Server objects in the module.

2> TCPServer class uses the internet TCP protocol, to provide continuous streams of data
between the client and server. The constructor automatically attempts to invoke
server_bind() and server_activate(). The other parameters are passed to the BaseServer
base class.

You must also create a subclass of StreamRequestHandler class. It provides self.rfile and
self.wfile attributes to read or write to get the request data or return data to the client.
     UDPServer and DatagramRequestHandler − These classes are meant to be used
        for UDP protocol.
     DatagramRequestHandler and UnixDatagramServer − These classes use Unix
        domain sockets; they're not available on non-Unix platforms.'''

''' Server Code
You must write a RequestHandler class. It is instantiated once per connection to the server,
and must override the handle() method to implement communication to the client.'''

import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        host,port=self.client_address
        print("{}:{} wrote:".format(host,port))
        print(self.data.decode())
        msg=input("enter text .. ")
        self.request.sendall(msg.encode())

''' On the server's assigned port number, an object of TCPServer class calls the forever()
method to put the server in the listening mode and accepts incoming requests from clients'''
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

''' Client Code
When working with socketserver, the client code is more or less similar with the socket
client application.
Example:- 
----------------
import socket
import sys
HOST, PORT = "localhost", 9999
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        data = input("enter text .. .")
        sock.sendall(bytes(data + "\n", "utf-8"))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("Sent: {}".format(data))
        print("Received: {}".format(received)) 
----------------
Run the server code in one command prompt terminal. Open multiple terminals for client
instances. You can simulate a concurrent communication between the server and more
than one clients.


Server                      Client-1                    Client-2
----------------------------------------------------------------
D:\socketsrvr>python        D:\socketsrvr>python        D:\socketsrvr>python
myserver.py                myclient.py                 myclient.py
127.0.0.1:54518 wrote:      enter text .. .             enter text .. .
from client-1              from client-1               from client-2
enter text ..              Sent: from client-1         Sent: from client-2
hello                      Received: hello             Received: hi client-2
127.0.0.1:54522 wrote:      enter text .. .             enter text .. .
how are you                how are you                 thanks
enter text ..              Sent: how are you           Sent: thanks
fine                       Received: fine              Received: bye client-2
127.0.0.1:54523 wrote:      enter text .. .             enter text .. .
from client-2              good bye                    
enter text ..              Sent: good bye              
hi client-2                Received: bye bye           
127.0.0.1:54526 wrote:      enter text .. .             
good bye                                               
enter text ..                                          
bye bye                                               
127.0.0.1:54530 wrote:                                 
thanks                                                
enter text ..                                         
bye client-2                                          
'''


