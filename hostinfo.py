#!/usr/bin/env python
import socket
import subprocess

import sys




# Ask for input
remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.remoteServer)
remoteServerEx = socket.gethostbyname_ex(remoteServer)
remoteok = True


print "-" * 60
print "Please wait, scanning remote host", remoteServerIP, remoteServerEx

print "-" * 60

try:
    for port in range(1, 1025):
        while remoteok:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #result = sock.connect_ex((remoteServerIP, port))
            #if socket.has_ipv6 == 1:
            if socket.has_ipv6 == True:
                print "supported"
                remoteok = False
            if socket.has_ipv6 == False:
                print "not"
                remoteok = False
        sock.close()

except KeyboardInterrupt:
    print "CONTROL C"
    sys.exit()

#subprocess.call('ping', shell=True
'echo hello'
