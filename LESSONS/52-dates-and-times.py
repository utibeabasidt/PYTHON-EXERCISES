import datetime

## DATE and TIME
date_time = datetime.datetime(2005, 3, 21, 19, 45, 21) # to get a specific date and time
print(date_time) # 2005-03-21 19:45:21

this_date_and_time = datetime.datetime.now() # getting date and time of now
print(this_date_and_time) # 2026-01-23 16:27:41.144439 (date and time)

this_date_and_time_format = datetime.datetime.now().strftime('%H:%M:%S %Y, %d, %m') # to get the date and time of now but in a string format
print(this_date_and_time_format) # 16:41:43 2026, 23, 01

## DATE
date = datetime.date(2025, 12, 31) # to get a specific date (year, month, date)
print(date) # 2025-12-31

today = datetime.date.today() # getting today's date
print(today) # 2026-01-23

today_format = datetime.date.today().strftime('%Y %m %d')
print(today_format) # 2026 01 23

# TIME
time = datetime.time(23, 13, 3) # to get a specific time (hours, mins, seconds)
print(time) # 23:13:03 (Note: Hours must be 24 or less)

this_time_format = datetime.datetime.now().strftime('%H %M %S') # getting the time, but in a string format
print(this_time_format) # 16 31 37

'''DATE TIME (specific, now and format now)
DATE (specific, today, and format today)
TIME (specific, and format now)'''