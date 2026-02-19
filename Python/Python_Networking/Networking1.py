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

'''----------------------------- Python - Socket Programming ---------------------------'''