#!/usr/bin/env python3

import socket
import sys
path = sys.argv[1]
print(path)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
addr = s.getsockname()[1]
s.close()

r = open("./output/docker-compose.yml","r")
data = r.read()
r.close()

#print(data)
data = data.replace('XXXX',str(addr))
data = data.replace('YYYY',path)
#print(data)
w = open("./output/docker-compose.yml","wt")
w.write(data)
w.close()

print("URL SET TO: http://localhost:" + str(addr))


