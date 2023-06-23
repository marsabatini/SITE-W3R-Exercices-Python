
# This program gets the name of the host on which
# the routine is runnig.

#Method 01
import socket
hostName = socket.gethostname()
print("Host name is: ", hostName)
print("-----")
print()

#Method 02
import platform
hostName = platform.uname()[1]
print("Host name is: ", hostName)
print("-----")
print()

#Method 03
import os
hostName = os.uname().nodename
print("Host name is: ", hostName)
print("-----")
print()