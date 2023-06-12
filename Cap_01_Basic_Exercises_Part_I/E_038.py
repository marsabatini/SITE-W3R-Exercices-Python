
    # The program solves the following remarkable product: (x + y) * (x + y)

def remProduct(x, y):

    result = (x * x) + (x * y) + (y * x) + (y * y)

    return print("({} + {})*({} + {}) = {}".format(x, y, x, y, result))

remProduct(4, 3)