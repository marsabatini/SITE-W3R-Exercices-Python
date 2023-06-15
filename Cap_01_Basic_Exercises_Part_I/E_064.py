
    # This program retrives the date and time od file creation and modificantion

import os.path, time

print("Last modified: %s" % time.ctime(os.path.getmtime("E_061.py")))
print("Created: %s" % time.ctime(os.path.getctime("E_061.py")))