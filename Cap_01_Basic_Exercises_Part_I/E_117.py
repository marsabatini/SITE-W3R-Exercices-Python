
# The program proves that two string variables
# of the same value points to the same memory
# location.

str1 = "Sabatini"
str2 = "Sabatini"

print("Memory location of str1:", hex(id(str1)))
print("M̀emory location of str2:", hex(id(str2)))