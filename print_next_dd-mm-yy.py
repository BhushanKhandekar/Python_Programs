year = int(input())
month = int(input())
day = int(input())

if year % 4 == 0:
    leap_year = True
else:
    leap_year = False

if month in (1,3,5,7,8,10,12):   # month
    month_len = 31
elif month == 2:
    if year % 4:
        month_len = 29
else:
    month_len = 30

if day < month_len:
    day+=1
else:
    day = 1

if month == 12:
    month = 1
    year += 1
else:
    if month < 12 and day == 1:
        month += 1

print(year, month, day)


