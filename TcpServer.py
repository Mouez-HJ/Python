import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print ("Connection from: " + str(addr))
    while True:
        print ("from connected user: " + str(data))
        data = c.recv(1024)
        if not data:
            break
        
        
        data = str(data).upper()
        print ("sending: " + str(data))
        byte_message = data.encode()
        c.send(byte_message)
    c.close()

if __name__ == '__main__':
    Main()
