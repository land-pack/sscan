import json
from socket import socket
from socket import AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST


def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

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
