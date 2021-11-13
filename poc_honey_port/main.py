import sys
import argparse
from socket import socket, AF_INET, SOCK_STREAM
import traceback

ADDRESS = "127.0.0.1" # Localhost

def honeypot(port):
    try:
        ski=socket(AF_INET,SOCK_STREAM)
        ski.bind((ADDRESS, port))
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
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Honeypot on port')
    parser.add_argument(
        '-p','--port', help='Port where server should listen for connections', 
        type=int,
        action='store',
        required=False,
        default=3389
    )   
    args = parser.parse_args()
    honeypot(args.port)