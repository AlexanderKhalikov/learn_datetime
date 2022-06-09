from datetime import datetime

DUE_DATE = datetime(year=2021, month=5, day=12, hour=8)
countdown = DUE_DATE - datetime.now()
print(f"Countdown to our wedding anniversary: {countdown}")
