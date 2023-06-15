
    # The program converts the distance (in feet) to inches,
    # yards and miles.


dFeet = int(input("Enter a distance in feet: "))
dInches = dFeet * 12
dYards = dFeet / 3.0
dMiles = dFeet / 5280.0

print("The distance in inches is %i inches." % dInches)
print("The distance in yards is %.2f yards." % dYards)
print("The distance in miles is %.2f miles." % dMiles)