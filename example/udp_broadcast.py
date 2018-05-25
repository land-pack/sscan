# On another machine I ran tcpdump:
# tcpdump -i eth1 port 54545 -XX

from socket import socket
from socket import AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST



cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
cs.sendto('This is a test', ('255.255.255.255', 54545))
