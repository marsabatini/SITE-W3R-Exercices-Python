
    # The program checks if the difference between a number x and 1000
    # is less than or equal to 100 and it repeats this same procedure
    # for the difference between a number x and 2000.

def near(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(near(1000))
print(near(900))
print(near(800))
print(near(2200))