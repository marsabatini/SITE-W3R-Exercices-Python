
    # The program calculates the greatest commom divisor (GCD)
    # of two positive integers

def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break

    return gcd

print("GCD of 12 and 17 is:", gcd(12, 17))
print("GCD of 4 and 6 is:", gcd(4, 6))
print("GCD of 336 and 360 is:", gcd(336, 360))