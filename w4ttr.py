#!/usr/bin/env python
import socket
import subprocess
yes = True
a = 0

while yes:
    print "run", a
    a = a+1
    if a == 5:
        yes = False
remoteServer = raw_input("Enter a remote host to scan: ")
p1 = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE)
output = p1.communicate()[0]
print output

if socket.has_ipv6:
        print "balls"

if not socket.has_ipv6:
        print "tits"