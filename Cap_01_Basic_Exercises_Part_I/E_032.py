
    # The program calculates the least commom multiple (LCM)
    # of two positive integers

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while(True):
        if (z % x == 0) and (z % y == 0):
            lcm = z
            break

        z += 1

    return lcm

print("LCM of 4 and 6 is:", lcm(4, 6))
print("LCM of 15 and 17 is:", lcm(15, 17))
print("LCM of 123 and 67 is:", lcm(123, 67))