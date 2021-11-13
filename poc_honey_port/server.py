import sys
from socket import socket, AF_INET, SOCK_STREAM
import traceback

DEFAULT_ADDRESS = "127.0.0.1" # Localhost

class Server:
    def __init__(self, address, port):
        try:
            self.acceptor = socket(AF_INET,SOCK_STREAM)
            self.acceptor.bind((address, port))
            self.acceptor.listen()
        except Exception:
            traceback.print_exc()
            sys.exit()

    def destroy(self):
        self.acceptor.close()

    def accept_connections(self):
        try:
            while True:
                conn,addr = self.acceptor.accept()
                print('honeypot has been visited by ' + addr[0])
                conn.close()
                # while True:
                #     data=conn.recv(1024)
                #     if data == b'\r\n':
                #         ski.close()
                #         sys.exit()
        except Exception:
            traceback.print_exc()
            self.destroy()
