
# This program gets numbers divisible by fifteen
# from a list using an anonymous function.

numList = [45, 55, 60, 37, 100, 105, 220]

divisible = list(filter(lambda x: (x % 15 == 0), numList))

print("Numbers divisible by 15:", divisible)