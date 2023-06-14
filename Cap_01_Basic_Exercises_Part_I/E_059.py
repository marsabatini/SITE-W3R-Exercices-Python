
    # The program converts height (in feet and inches) to centimeters.


print("Enter the height")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("The height is: %s cm." % h_cm)