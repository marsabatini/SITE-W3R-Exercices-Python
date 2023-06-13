
    # The program parses a string to float or integer.

#Method 01
n = "123.3123"

print("Method 01")
print(float(n))
print(int(float(n)))


#Method 02
def convert(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

print('\nMethod 02')
print(convert('12'))
print(convert('123.53123'))