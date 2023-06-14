
    # The program calculates the hypotenuse of right angled triangle.

from math import sqrt

print("Enter lengths of shorter triangle sides: ")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c)