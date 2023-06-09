
    # The program calculates the sum of three numbers.
    # If the values are equal, then it returns thrice
    # of their sum.

def thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3

    return sum

print(thrice(2, 4, 6))
print(thrice(2, 2, 2))


