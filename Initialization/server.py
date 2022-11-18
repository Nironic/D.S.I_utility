client = []

def hides(sock):
    global client
    y = 0
    while True:
        s, addr = sock.accept()
        if s in client:
            pass
        else:
            client.append(s)

def init():
    global client
    ip = "192.168.1.223"
    import socket
    from threading import Thread
    sock = socket.socket()
    sock.bind((ip, 4455))
    sock.listen(1000)
    Thread(target=hides, args=(sock,)).start()    

    while True:
        print(client)
