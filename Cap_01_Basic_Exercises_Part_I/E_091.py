
# The program swaps two variable

def swap(x, y):
    temp = x
    x = y
    y = temp

    print("New values: x = %d and y = %d" % (x, y))


x = 20
y = 60

print("Original values: x = %d and y =%d" % (x, y))
print(swap(x, y))