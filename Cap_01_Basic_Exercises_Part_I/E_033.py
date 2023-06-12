
    # The program sums three given integers.
    # However, if two values are equals, the sum will be zero.


def sum(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x + y + z

    return sum

print("The sum of 2, 1 and 2 is:", sum(2, 1, 2))
print("The sum of 1, 2 and 6 is", sum(1, 2, 6))