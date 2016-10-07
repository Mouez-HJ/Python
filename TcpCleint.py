import socket
def Main():
        host ='127.0.0.1'
        port = 5000

        s = socket.socket()
        s.bind((host, port))

        message = raw_input("->")
        while message != 'q':
               s.send(messge)
               data = soc.recv(1024)
                           
               message = raw_input(("->")

               
    s.close()
if __name__ == '__main__':
            Main()
            


                                           
                                           

                                           
