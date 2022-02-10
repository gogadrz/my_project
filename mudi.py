import datetime

# = datetime.date(2022, 2, 10)

date_str = '10-02-2022'

full_date = datetime.datetime.strptime(date_str, '%d-%m-%Y')
print(full_date.day)
print(full_date.month)
print(full_date.year)

