# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import random

host = sys.argv[1]
textport = sys.argv[2]
number = int(sys.argv[3])


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
increment = 0
    
for x in range(number):
        data = random.randint(1,101)
        print (data)
        
        
        #s.sendall(data.encode('utf-8'))
        #Sending response
        print("Sending %s" % data)
        data1=str(data)
        s.sendto(data1.encode('utf-8'),server_address)

s.shutdown(1)