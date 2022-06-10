from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain
print(delta)

# Boolean
delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta2 != delta1)
print(delta2 == 5)

# Normalization

year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)
year == another_year

print(year.total_seconds())

# arithmetic

year = timedelta(days=365)
ten_years = 10 * year
print(ten_years)

ten_years.days // 365

nine_years = ten_years - year
print(nine_years)

three_years = nine_years // 3
print(three_years, three_years.days // 365)


