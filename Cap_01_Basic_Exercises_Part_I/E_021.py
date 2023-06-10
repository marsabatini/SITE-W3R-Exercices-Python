
    # The program shows whether a given number is even or odd.
    # Then, it prints an appropriate message to the user.

num = int(input("Enter a number: "))
mod = num % 2

if mod > 0:
    print("The number is odd.")
else:
    print("The number is even.")
