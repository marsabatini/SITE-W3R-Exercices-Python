
    # The program sums two values, if both are integers.

def sumIntegers(x, y):

    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        return "The values are not integers."

print(sumIntegers(10, 20))
print(sumIntegers(10, 23.42))
print(sumIntegers('2', 3))