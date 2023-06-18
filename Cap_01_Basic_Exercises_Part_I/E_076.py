
# The program gets the command-line arguments
# (name of the script, the number of arguments,
# arguments) passed to a script.

import sys

print("This is the path of the script:", sys.argv[0])
print("The number of arguments:", len(sys.argv))
print("Argument List:", str(sys.argv))
