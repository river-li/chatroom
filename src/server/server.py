import socket
from multi_task import ClientThread, User

def log(msg):
    with open('server.log', 'a') as f:
        f.write(msg+'\n')


class Server():

    def __init__(self, addr):
        self.ADDR = addr

    def run(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_sock.bind(self.ADDR)
            server_sock.listen(5)
        except Exception as e:
            print(e)
            server_sock.shutdown(0)
            server_sock.close()

        threads = []

        while True:
            try:
                log("Waiting for Connection ...")
                client_sock, addr = server_sock.accept()
                log("Connected from: "+str(addr))

                user = User(addr, client_sock)
                client_thread = ClientThread(user)

                threads += [client_thread]

                client_thread.start()

            except Exception as e:
                print(e)
                log(str(e))
                for t in threads:
                    t.stop()
                break

        server_sock.close()

def main():
    HOST = '127.0.0.1'
    PORT = 8001
    ADDR = (HOST, PORT)
    server = Server(ADDR)
    server.run()

if __name__ == '__main__':
    main()
