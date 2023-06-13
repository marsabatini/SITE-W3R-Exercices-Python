
    # This program determines if a Python shell is executing
    # in 32 bits or 64 bits mode on OS.

import platform, struct

#Method 01
print("Method 01")
print(struct.calcsize("P") * 8)


#Method 02
print("\nMethod 02")
print(platform.architecture()[0])

