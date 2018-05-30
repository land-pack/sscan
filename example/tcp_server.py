import socket
import time

###bash-3.2# ps -ef | grep tcp_server
###  503 35444  6974   0  8:00AM ttys007    0:00.04 python tcp_server.py
###    0 35486 35468   0  8:00AM ttys011    0:00.01 grep tcp_server
###bash-3.2# dtruss -p 35444

#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind(('localhost', 9094))
#become a server socket
serversocket.listen(2)

# Client ---syn --->
#        <--RST ----  Server

counter = 0

while 1:
    counter = counter + 1
    print("sleep 3 seconds")
    time.sleep(3)
    if counter > 20:
        break

while 1:
    #time.sleep(1000)    
    conn, addr = serversocket.accept()
    while True:
        d = conn.recv(1024)
        if d:
            print(d)
        else:
            print("No more data")
            break
    # if i add close call at the end of this loop
    conn.close()

# do no accept ... see what the TCP doing
# is finish three-hand-shack.
print('Done.')
