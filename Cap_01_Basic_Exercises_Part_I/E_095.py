
# The program checks whether a string is numeric

def checkString(str):
    try:
        i = float(str)
        x = "Numeric"
    except(ValueError, TypeError):
       x = "Not numeric."

    return x


str1 = "123456"
str2 = "abc123"

print(checkString(str1))
print(checkString(str2))



