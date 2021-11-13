import argparse

DEFAULT_ADDRESS = "127.0.0.1" # localhost
DEFAULT_PORT = 3389

def _config_parser(parser):
    parser.add_argument(
        '-a','--address', help='Address of the server (default=%s)' % DEFAULT_ADDRESS, 
        type=str,
        action='store',
        required=False,
        default=DEFAULT_ADDRESS
    )
    parser.add_argument(
        '-p','--port', help='Port where server should listen for connections (default=%i)' % DEFAULT_PORT, 
        type=int,
        action='store',
        required=False,
        default=DEFAULT_PORT
    )

def parse():
    parser = argparse.ArgumentParser(description='Honeypot on port')
    _config_parser(parser)
    return parser.parse_args()