
    # The program gets the current username

#Method 01
import getpass

print("Method 01")
print(getpass.getuser())


#Method 02
import os
import pwd

def getUsername():
    return pwd.getpwuid(os.getuid()) [0]

print("\nMethod 02")
print(getUsername())