
    # The program calculates the number of days between two dates.

    # For that, it uses the datatime function that returns a date
    # object with same year, month and day.


from datetime import date

firstDate = date(2014, 7, 2)
lastDate = date(2023, 6, 9)

result = lastDate - firstDate

print(f"The number of days passed was: {result.days} days.")



