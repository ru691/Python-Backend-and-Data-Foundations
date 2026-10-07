import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week) #rmb counting starts from 0, 0 = mon, 1 = tues, 2 = wed and so forth
if year == 2026 :
    print("Hello World")

date_of_birth = dt.datetime(year=2005, month=10, day=18)
print(date_of_birth)