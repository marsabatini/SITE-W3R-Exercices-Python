
# The program asks the user to enter a series of numbers separated
# by comma to form a list and tuple.
# It then uses the split() method to separete the values and to form
# the list and tuple.

values = input("Enter some comma-separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List:\t", list)
print("Tuple:\t", tuple)