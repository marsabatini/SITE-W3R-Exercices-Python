
    # This program gets OS name, platform and release information.

import platform
import os
import sys
import sysconfig

#Method 01
print("Method 01")
print("Name of the operanting system:", os.name)
print("Name of the OS:", platform.system())
print("Version of the OS:", platform.release())


#Method 02
print("Method 02")
print("os.name:                      ", os.name)
print("sys.platform:                 ", sys.platform)
print("sysconfig.get_platform:       ", platform.system())
print("platform.machine():           ", platform.machine())
print("platform.architecture:        ", platform.architecture())