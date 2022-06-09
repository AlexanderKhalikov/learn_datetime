# The three classes that represent dates and times in datetime have similar initializers.
# They can be instantiated by passing keyword arguments for each of the attributes,
# such as year, date, or hour. You can try the code below to get a sense of how each object is created:

from datetime import date, time, datetime
print(date(year=2020, month=1, day=31))

print(time(hour=13, minute=14, second=31))

print(datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31))

print(f'With f-strings {date.today():%m/%d/%Y}')

now = datetime.now()

print(f'{now:%Y-%m-%d %H:%M}')
