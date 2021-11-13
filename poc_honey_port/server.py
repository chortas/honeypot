import sys
from socket import socket, AF_INET, SOCK_STREAM
import traceback

DEFAULT_ADDRESS = "127.0.0.1" # Localhost

def accept_connections(port):
    try:
        ski=socket(AF_INET,SOCK_STREAM)
        ski.bind((DEFAULT_ADDRESS, port))
        ski.listen()
        conn,addr = ski.accept()
        print('honeypot has been visited by ' + addr[0])
        while True:
            data=conn.recv(1024)
            if data == b'\r\n':
                ski.close()
                sys.exit()
    except Exception:
        traceback.print_exc()
        ski.close()
        sys.exit()
