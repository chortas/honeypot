import socket as skt_lib
from socket import socket, AF_INET, SOCK_STREAM
import time

class Server:
    def __init__(self, address, port, timeout):
        self.acceptor = socket(AF_INET,SOCK_STREAM)
        self.acceptor.bind((address, port))
        self.acceptor.listen()
        self.timeout = timeout
        print("[Honeypot] Started up")

    def destroy(self):
        self.acceptor.close()
        print("[Honeypot] Closed acceptance socket")

    def handle_connection(self, conn, addr):
        ip = addr[0]
        print("[Honepot] Attacker's IP address: " + ip)
        conn.settimeout(self.timeout)
        start = time.time()
        try:
            print("[Honepot] Attacker sent:")
            while True:
                data = conn.recv(1024)
                end = time.time()
                if not len(data):
                    print('[Honeypot] Attacker closed connection')
                    break
                print(data)
                if (end - start) > self.timeout:
                    raise skt_lib.timeout
        except skt_lib.timeout:
            print('[Honeypot] Connection timeout reached')
            pass
        finally:
            conn.close()
            print('[Honeypot] Closed connection')      

    def accept_connections(self):
        try:
            while True:
                conn,addr = self.acceptor.accept()
                print('== BEGIN ==')
                self.handle_connection(conn, addr)
                print('== END ==')
        except KeyboardInterrupt:
            print("[Honeypot] Shutting down")
            pass
        except Exception as e:
            raise e
        finally:
            self.destroy()
