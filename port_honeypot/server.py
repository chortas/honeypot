import socket as skt_lib
from socket import socket, AF_INET, SOCK_STREAM
import time

class Server:
    def __init__(self, address, port, timeout, logger):
        self.acceptor = socket(AF_INET,SOCK_STREAM)
        self.acceptor.bind((address, port))
        self.acceptor.listen()
        self.timeout = timeout
        self.logger = logger
        logger.info("[Honeypot] Started up")

    def destroy(self):
        self.acceptor.close()
        self.logger.info("[Honeypot] Closed acceptance socket")

    def handle_connection(self, conn, addr):
        ip = addr[0]
        self.logger.info("[Honepot] Attacker's IP address: " + ip)
        conn.settimeout(self.timeout)
        start = time.time()
        try:
            self.logger.info("[Honepot] Attacker sent:")
            while True:
                data = conn.recv(1024)
                end = time.time()
                if not len(data):
                    self.logger.info('[Honeypot] Attacker closed connection')
                    break
                self.logger.info(data)
                if (end - start) > self.timeout:
                    raise skt_lib.timeout
        except skt_lib.timeout:
            self.logger.info('[Honeypot] Connection timeout reached')
            pass
        finally:
            conn.close()
            self.logger.info('[Honeypot] Closed connection')      

    def accept_connections(self):
        try:
            while True:
                conn,addr = self.acceptor.accept()
                self.logger.info('== BEGIN ==')
                self.handle_connection(conn, addr)
                self.logger.info('== END ==')
        except KeyboardInterrupt:
            self.logger.info("[Honeypot] Shutting down")
            pass
        except Exception as e:
            raise e
        finally:
            self.destroy()
