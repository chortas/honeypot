import argparse

DEFAULT_ADDRESS = "127.0.0.1" # localhost
DEFAULT_PORT = 3389
DEFAULT_TIMEOUT_S = 1 # In secondos
DEFAULT_FILE = "output.log"

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
    parser.add_argument(
        '-t','--timeout', help='Time before closing attacker connection, while the server will gather its input (default=%f)' % DEFAULT_TIMEOUT_S, 
        type=float,
        action='store',
        required=False,
        default=DEFAULT_TIMEOUT_S
    )
    parser.add_argument(
        '-f','--filename', help=f'File to which the logging output will be written (default={DEFAULT_FILE})',
        type=str,
        action='store',
        required=False,
        default=DEFAULT_FILE
    )

def parse():
    parser = argparse.ArgumentParser(description='Honeypot on port')
    _config_parser(parser)
    return parser.parse_args()