import sys
import argparse
from socket import socket, AF_INET, SOCK_STREAM
import traceback

def honeypot(address, port=3389):
    try:
        ski=socket(AF_INET,SOCK_STREAM)
        ski.bind((address, port))
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
    parser.add_argument('-a','--address', help='server ip address to use', action='store', required=True)   
    args = parser.parse_args()
    honeypot(args.address)