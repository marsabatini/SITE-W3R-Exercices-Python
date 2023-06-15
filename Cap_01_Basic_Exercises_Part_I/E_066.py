
    # The program calculates the body mass index.

height = float(input("Enter your height in feet: "))
weight = float(input("Enter yout weight in feet: "))

print("Your body mass index is: ", round(weight / (height * height), 2))