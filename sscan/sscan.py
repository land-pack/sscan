from utils.hosts import get_ip


import tornado.ioloop
import tornado.web
import tornado.websocket

import json
from socket import socket
from socket import AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST

def attentionPlease():
    """
    Get self host information and then
    broadcast it out.
    """
    cs = socket(AF_INET, SOCK_DGRAM)
    cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    host_info = {
        "ip": get_ip(),
        "port": 8888,
        "path": "/ws"
    }
    cs.sendto(json.dumps(host_info), ('255.255.255.255', 54545))


class EchoWebSocket(tornado.websocket.WebSocketHandler):

    def check_origin(self, handler):
        return True

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

def make_app():
    return tornado.web.Application([
        (r"/ws", EchoWebSocket),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.PeriodicCallback(attentionPlease, 1000 * 5).start()
    tornado.ioloop.IOLoop.current().start()
