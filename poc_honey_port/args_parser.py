import argparse

DEFAULT_PORT = 3389

def _config_parser(parser):
    parser.add_argument(
        '-p','--port', help='Port where server should listen for connections', 
        type=int,
        action='store',
        required=False,
        default=DEFAULT_PORT
    )

def parse():
    parser = argparse.ArgumentParser(description='Honeypot on port')
    _config_parser(parser)
    return parser.parse_args()