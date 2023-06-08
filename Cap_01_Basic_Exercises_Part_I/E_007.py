
# The code asks the user for enter the filename
# in order to return the file extension.
# Note that it uses the split() method with [-1]
# to return the desired "side" od the slit.

filename = input("Please, enter the filename: ")
f_ext = filename.split(".")
print("The extension of the file is: " + repr(f_ext[-1]))