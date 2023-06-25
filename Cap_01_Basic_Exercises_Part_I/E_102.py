
# This program gets system command output.

import subprocess

returnedText = subprocess.check_output("ls", shell=True, universal_newlines=True)
print(returnedText)