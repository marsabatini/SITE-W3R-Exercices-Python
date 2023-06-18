
# This code gets the size of an object in bytes.

import sys

str1 = "one"
str2 = "four"
str3 = "three"

x = 0
y = 112
z = 122.56

print("Size of ", str1, "=", str(sys.getsizeof(str1)) + " bytes.")
print("Size of ", str2, "=", str(sys.getsizeof(str2)) + " bytes.")
print("Size of ", str3, "=", str(sys.getsizeof(str3)) + " bytes.")
print("Size of", x, "=" ,str(sys.getsizeof(x)) + " bytes.")
print("Size of" ,y , "=" + str(sys.getsizeof(y)) + " bytes.")

L = [10, 21, 7, 'Yellow', 'Blue']
print("Size of", L, "=", sys.getsizeof(L), " bytes.")

T = ("Green", [12, 5, 9], (1, 2, 3))
print("Size of", T, "=", sys.getsizeof(T), " bytes.")

S = {'apple', 'orange', 'apple', 'pear'}
print("Size of", S, "=", sys.getsizeof(S), " bytes.")

D = {'Name': 'David', 'Age': 6, 'Class': 'First'}
print("Size of", D, "=", sys.getsizeof(S), " bytes.")