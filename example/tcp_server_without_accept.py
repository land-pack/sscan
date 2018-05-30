import socket
import time

#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 9092))
#become a server socket
serversocket.listen(5)

# Client ---syn --->
#        <--RST ----  Server

while 1:
    time.sleep(1000)    

# do no accept ... see what the TCP doing
# is finish three-hand-shack.
print('Done.')
