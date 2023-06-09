
    # The program gets a new string from n copies.

def newString(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result

print(newString('_Marco_', 2))
print(newString('py', 5))