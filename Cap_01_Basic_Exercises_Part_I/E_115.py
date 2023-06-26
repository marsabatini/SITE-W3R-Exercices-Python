
# This program computes the product of a list
# of integers (without using a for loop).

#Method 01
from functools import reduce

nums = [10, 20, 30]

print("The original list:", nums)

numsProduct = reduce((lambda x, y: x * y), nums)
print("Product:", numsProduct)
print()

#Method 02
import math

nums = [10, 20, 30]

print("The original list:", nums)

numsProduct = math.prod(nums)
print("Product:", numsProduct)