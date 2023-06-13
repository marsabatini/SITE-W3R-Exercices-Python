
    # The program checks a file exists.


# Method 01
import os.path

print("#Method 01")
print(os.path.isfile("E_040.py"))
print(os.path.isfile("noExist.py"))


# Method 02
print("\nMethod 02")
print(os.path.exists("E_040.py"))
print(os.path.exists("noExist.py"))


# Method 03
myFile = open("E_040.py")

print("\nMethod 03")

try:
    myFile.close()
    print("File found.")
except FileNotFoundError:
    print("File not found.")