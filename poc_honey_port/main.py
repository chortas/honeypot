import args_parser
import server as svr
    
if __name__ == '__main__':
    args = args_parser.parse()
    server = svr.Server(args.address, args.port)
    server.accept_connections()