import socket
def Main():
        host ='127.0.0.1'
        port = 5000

        s_client = socket.socket()
        s_client.connect((host, port))
        
        message = raw_input("->")
        while message != 'q':
               s_client.send(messge)
               data = s_client.recv(1024)
               print 'Received from server: ' + str(data)
               message = raw_input("->")
        s_client.close()
if __name__ == '__main__':
    Main()
            
        
               
