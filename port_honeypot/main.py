import args_parser
import server as svr
import sys
from logger import create_logger
    
if __name__ == '__main__':
    try:
        args = args_parser.parse()
        logger = create_logger(args.filename)
        server = svr.Server(args.address, args.port, args.timeout, logger)
        server.accept_connections()
    except Exception as e:
        print(str(e))
        sys.exit(1)
