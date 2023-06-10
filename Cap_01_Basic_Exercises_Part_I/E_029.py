
    # The code prints out all colors from a first list of colors
    # that are not present in a second list of color.

colorsList_1 = set(['White', 'Black', 'Red'])
colorsList_2 = set(['Red', 'Green'])

print("Original set elements:")
print(colorsList_1)
print(colorsList_2)

print("\nDifferenct of colorsList_1 and colorsList_2:")
print(colorsList_1.difference(colorsList_2))
print("\nDifferenct of colorsList_2 and colorsList_1:")
print(colorsList_2.difference(colorsList_1))