from datetime import datetime


f_str = "b d Y - H:M:S"
dt, tm = f_str.split(' - ')

month, day, year = map(str, dt.split())
hours, minutes, secs = map(str, tm.split(':'))
now = datetime.now()

str_format = '%{month} %{day} %{year} - %{hours}:%{minutes}:%{secs}'.format(
    month=month,
    day=day,
    year=year,
    hours=hours,
    minutes=minutes,
    secs=secs
)
print(now.strftime(str_format))
