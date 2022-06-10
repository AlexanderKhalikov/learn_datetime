from datetime import datetime
import time

DUE_DATE = datetime(year=2022, month=6, day=11, hour=5)
countdown = DUE_DATE - datetime.now()
print(f"Countdown to our wedding anniversary: {countdown}")

while True:
    print(DUE_DATE - datetime.now())
    time.sleep(3)
