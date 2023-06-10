
    # The program concatenates all elements in a list
    # into a string and returns it.


def concatenate(list):

    result = ""

    for element in list:
        result += str(element)

    return result


print(concatenate([1, 5, 6, 4, 2]))