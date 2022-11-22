import datetime
from datetime import date,time

help(date)

today = date(2022,11,17)
print(today)

print(today.year)
print(today.month)
print(today.day)

w=today.weekday()
print('요일 정보:', w)

help(time)

currTime = time(21,4,30)
print(currTime)

print(currTime.hour)
print(currTime.minute)
print(currTime.second)

isoTime = currTime.isoformat()
print(isoTime)
