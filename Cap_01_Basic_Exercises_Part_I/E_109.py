
# The program checks if number is positive, negative or zero.

def check(x):

    if x > 0:
        return "Number positive."
    elif x < 0:
        return "Number negative."
    else:
        return "Number zero."

x = float(input("Enter your number: "))
print(check(x))