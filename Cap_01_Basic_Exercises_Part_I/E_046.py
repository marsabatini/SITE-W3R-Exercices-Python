
    # This program retrieves the path and name file currently begin executed.

import os

print("Current File Name:", os.path.realpath(__file__))