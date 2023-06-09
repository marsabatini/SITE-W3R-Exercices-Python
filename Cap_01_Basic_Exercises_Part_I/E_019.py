
    # The program gets a new string from a given string
    # where "is" has been added to the front.

def newString(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text

print(newString("Array"))
print(newString("IsEmpty"))