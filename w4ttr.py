#!/usr/bin/env python
import socket
import subprocess
yes = True
a = 0

while yes:
remoteServer = raw_input("Enter a remote host to scan: ")

if socket.has_ipv6:
        print "Has IPv6"

if not socket.has_ipv6:
        print "Does Not Have IPv6"
