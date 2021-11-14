from socket import socket, AF_INET, SOCK_STREAM

class Server:
    def __init__(self, address, port):
        self.acceptor = socket(AF_INET,SOCK_STREAM)
        self.acceptor.bind((address, port))
        self.acceptor.listen()

    def destroy(self):
        self.acceptor.close()

    def handle_connection(self, _conn, _addr):
        pass

    def accept_connections(self):
        try:
            while True:
                conn,addr = self.acceptor.accept()
                print('[Honeypot] Accepted connection from ' + addr[0])
                self.handle_connection(conn, addr)
                conn.close()
                print('[Honeypot] Closed connection from ' + addr[0])
        except KeyboardInterrupt:
            print("[Honeypot] Shutting down.")
            pass
        except Exception as e:
            raise e
        finally:
            self.destroy()
