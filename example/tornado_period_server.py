from socket import socket
from socket import AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST

import tornado.ioloop
import tornado.web



def attentionPlease():
    """
    Get self host information and then
    broadcast it out.
    """
    cs = socket(AF_INET, SOCK_DGRAM)
    cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    cs.sendto('This is a test', ('255.255.255.255', 54545))



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.PeriodicCallback(attentionPlease, 1000 * 5).start()
    tornado.ioloop.IOLoop.current().start()
