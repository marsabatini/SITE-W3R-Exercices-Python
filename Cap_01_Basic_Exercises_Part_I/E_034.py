
    # The program sum two given integers.
    # However, if the sum is between 15 and 20, it will return 20.

def sum(x, y):
    sum = x + y

    if sum >= 15 and sum <= 20:
        sum = 20

    return sum

print("The sum of 10 and 06 is:", sum(10, 6))
print("The sum of 10 and 02 is:", sum(10, 2))
print("The sum of 10 and 12 is:", sum(10, 12))