
    # The program calculates the difference between a given number
    # and 17. If the number is greater than 17, it returns twice
    # the absolute difference.

def difference(n):
    if n <= 17:
        return 17 - n;
    else:
        return (n - 17) * 2

n = int(input("Enter a number: "))
print("The difference between 17 and the number entered is: ", difference(n))
print("The double of the difference between 17 and 22 is:   ", difference(22))