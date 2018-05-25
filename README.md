# sscan
Node automatic discovery server and join it base on tornado UDP broadcast . Connect by TCP


How does it work?
======

Server will send broadcast which include server host-port to the local-network.
if there any node alive , will read this data and then try to connect to the Server
and all node can be die any time so we will do broadcast period time. the period time
can be configuration as you like.
