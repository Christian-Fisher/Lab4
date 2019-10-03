# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json
 
host = sys.argv[1]
textport = sys.argv[2]
num = int(sys.argv[3])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
count=1
x={
    "name":"John", 
    "age":30,
    "city":"New York"
    }
print(x)
while (count<=num):
        data=json.dumps(x)
        s.sendto(data.encode('utf-8'), server_address)
        x["age"]= x["age"] +1        
        count+=1
        
s.shutdown(1)

