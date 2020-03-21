import socket

dest_ip = "127.0.0.1"
dest_port = 50000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((dest_ip,dest_port))

while True:
    message = input("Please enter your message: ")
    if(len(message)==0):
        break
    message = message.encode('utf-8')
    client.send(message)
    data = client.recv(1024)
    print("[*] "+data.decode('utf-8'))
