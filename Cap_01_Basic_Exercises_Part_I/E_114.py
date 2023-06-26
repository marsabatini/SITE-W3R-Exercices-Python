
# This code filters positive numbers from a list.

nums = [34, 1, 0, -23, 12, -88]

print("The original list is:", nums)

newNums = list(filter(lambda x: x > 0, nums))
print("The new list is:", newNums)