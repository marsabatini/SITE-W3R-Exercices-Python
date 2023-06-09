
    # This code prints the days of the month  from the year and month entered.

    # It uses the calendar module allowing the use
    # of several functions of this class.

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

print(calendar.month(year, month))