
    # The program returns true, if the tow given integer values
    # are equal or their sum or difference is 5.

def testNumer(x, y):

    if x == y or (x + y) == 5 or abs(x - y) == 5:
        return True
    else:
        return False

print(testNumer(7, 2))
print(testNumer(3, 2))
print(testNumer(2, 2))
print(testNumer(7, 3))
print(testNumer(40, 4))
