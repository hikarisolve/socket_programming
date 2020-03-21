import socket
import threading
from function import clientThreadFunc

ip_addr = "127.0.0.1"
port = 50000

n = int(input("enter the number to listen: "))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((ip_addr,port))

server.listen(n)

while True:
    conn,addr = server.accept()

    client_thread = threading.Thread(target=clientThreadFunc,args=(conn,addr))

    client_thread.start()
