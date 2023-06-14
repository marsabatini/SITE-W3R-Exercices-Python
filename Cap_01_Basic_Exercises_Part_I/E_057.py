
    # The code gets the execution time of a Python method.

import time

def sumN_Number():
    startTime = time.time()
    s = 0

    for i in range(1, n + 1):
        s = s + i

    endTime = time.time()

    return s, endTime - startTime

n = 5
print("\nTime to sum of 1 to", n, " and requerid time to calculate is: ", sumN_Number(n))