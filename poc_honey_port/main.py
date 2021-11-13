import args_parser
import server
    
if __name__ == '__main__':
    args = args_parser.parse()
    server.accept_connections(args.address, args.port)