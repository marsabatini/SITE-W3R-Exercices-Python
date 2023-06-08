
# The program calculates the area of a circle based on the radius entered by the user.

from math import pi

radius = float(input("Please, input the radius of the circle: "))
print("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))