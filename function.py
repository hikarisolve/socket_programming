
def clientThreadFunc(conn,addr):
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if(len(data)==0):
            break
        print("[*] Recieved: [%s] from %s:%d"%(data,addr[0],addr[1]))
        conn.send("Receipt completed".encode('utf-8'))
    conn.close()
