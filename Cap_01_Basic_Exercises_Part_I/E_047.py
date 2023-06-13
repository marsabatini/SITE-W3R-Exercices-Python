
    # The code finds out the number of CPUs used.

import multiprocessing
import os

#Method 01
print("Method 01")
print("The number of CPUs used is:", multiprocessing.cpu_count())

#Method 02
print("\nMethod 02")
print("The number of CPUs used is:", os.cpu_count())