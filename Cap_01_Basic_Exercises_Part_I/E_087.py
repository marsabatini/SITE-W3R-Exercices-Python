
# The program gets the size of a file.

import os

#Method 01
fileSize = os.path.getsize("E_001.py")
print("\nThe size of E_001.py is:", fileSize, "bytes.")

#Method 02
fileSize2 = os.stat("E_002.py")
print("The size of E_002.py is:", fileSize2.st_size, "bytes.")

#Method 03
file = open("E_003.py")
file.seek(0, os.SEEK_END)
print("The size os E_003.py is:", file.tell(), "bytes.")