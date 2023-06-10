
    # The program checks whether a specified value is
    # contained within a group of values.


def is_group(group, n):

    for value in group:
        if n == value:
            return True

    return False

print(is_group([1, 2, 4, 5, 5, 7], 4))
print(is_group([5, 2, 6, 7], 9))