# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time


textport = sys.argv[1]


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
    buf, address = s.recvfrom(port)
    
    if not len(buf):
        break
    #buf1 = int.from_bytes(buf,"little")
    buf1=str(buf, 'utf-8')
    print ("Received %s bytes from %s " % (buf1, address ))
    print("ACK: %s" % buf1)
        
s.shutdown(1)