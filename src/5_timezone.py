import pytz
import datetime

tz_berlin = pytz.timezone("Europe/Berlin")
dt_berlin =datetime.datetime.now(tz_berlin)
print(dt_berlin)

# Convert timezone


timezone_berlin = '2019-06-29 17:08:00'
tz_ber_obj = datetime.datetime.strptime(timezone_berlin, '%Y-%m-%d %H:%M:%S')
timezone_newyork = pytz.timezone('America/New_York')
timezone_newyork_obj = timezone_newyork.localize(tz_ber_obj)
print(timezone_newyork_obj)
print(timezone_newyork_obj.tzinfo)
