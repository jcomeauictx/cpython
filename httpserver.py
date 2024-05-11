#!/usr/local/jcpython/bin/python3
import http.server
del http.server.__all__  # otherwise the following will only get classes
from http.server import *
from http.server import test as original_test

class BaseHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    '''
    Same as original but adds default content-type
    '''
    default_content_type = "application/octet-stream"

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler,
                               BaseHTTPRequestHandler):
    '''
    Same as original but defaults to default_content_type

    Also uses a simpler, short-circuiting, guess_type method, which may
    break some obscure uses of empty content-type headers.
    '''
    def guess_type(self, path):
        '''
        Find and return what we think would be the most fitting mime-type
        for the content, based solely on the file extension.
        '''
        base, ext = posixpath.splitext(path)
        return self.extensions_map.get(ext) or \
            self.extensions_map.get(ext.lower()) or \
            mimetypes.guess_type(path)[0] or \
            self.default_content_type

def test(HandlerClass=BaseHTTPRequestHandler,
         ServerClass=ThreadingHTTPServer,
         protocol="HTTP/1.0", port=8000, bind=None,
         content_type=BaseHTTPRequestHandler.default_content_type):
    '''
    Adds defaut content-type to http.server.test.
    '''
    HandlerClass.default_content_type = content_type
    original_test(HandlerClass, ServerClass, protocol, port, bind)

# the following is copied mostly verbatim from the Lib module.
if __name__ == '__main__':
    import argparse
    import contextlib

    parser = argparse.ArgumentParser()
    parser.add_argument('--cgi', action='store_true',
                        help='run as CGI server')
    parser.add_argument('-b', '--bind', metavar='ADDRESS',
                        help='bind to this address '
                             '(default: all interfaces)')
    parser.add_argument('-d', '--directory', default=os.getcwd(),
                        help='serve this directory '
                             '(default: current directory)')
    parser.add_argument('-p', '--protocol', metavar='VERSION',
                        default='HTTP/1.0',
                        help='conform to this HTTP version '
                             '(default: %(default)s)')
    parser.add_argument('--content-type',  # parsed into content_type
                        default=BaseHTTPRequestHandler.default_content_type,
                        help='sets default content type for unknown extensions')
    parser.add_argument('port', default=8000, type=int, nargs='?',
                        help='bind to this port '
                             '(default: %(default)s)')
    args = parser.parse_args()
    if args.cgi:
        handler_class = CGIHTTPRequestHandler
    else:
        handler_class = SimpleHTTPRequestHandler

    # ensure dual-stack is not disabled; ref #38907
    class DualStackServer(ThreadingHTTPServer):

        def server_bind(self):
            # suppress exception when protocol is IPv4
            with contextlib.suppress(Exception):
                self.socket.setsockopt(
                    socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
            return super().server_bind()

        def finish_request(self, request, client_address):
            self.RequestHandlerClass(request, client_address, self,
                                     directory=args.directory)

    test(
        HandlerClass=handler_class,
        ServerClass=DualStackServer,
        port=args.port,
        bind=args.bind,
        protocol=args.protocol,
        content_type=args.content_type
    )
