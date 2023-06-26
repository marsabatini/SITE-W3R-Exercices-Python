
# This program inputs a number and generates an error
# mensage if it is not a number.

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again.")