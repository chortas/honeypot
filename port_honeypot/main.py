import args_parser
import server as svr
import sys
    
if __name__ == '__main__':
    try:
        args = args_parser.parse()
        server = svr.Server(args.address, args.port, args.timeout)
        server.accept_connections()
    except Exception as e:
        print(str(e))
        sys.exit(1)