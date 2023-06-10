
    # The code creates a histogram from a given list of integers.

def histogram(items):

    for n in items:
        output = ""
        times = n

        while times > 0:
            output += '*'
            times = times - 1

        print(output)

histogram([2, 5, 7, 2, 1])