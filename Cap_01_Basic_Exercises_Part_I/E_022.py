
    # The program counts the number 4 in a given list.

def list_count(nums):
    count = 0

    for num in nums:
        if num == 4:
            count = count + 1

    return count

print(list_count([1, 2, 4, 7, 4, 9]))