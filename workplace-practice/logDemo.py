import logging
from datetime import datetime, timezone, timedelta
import time


#logging.info("this")

# Create Time UTC + 8
now = datetime.utcnow()
print(now)
utc_8 = timezone(timedelta(hours=8))
now = now.replace(tzinfo=timezone.utc)
print(now)
time_now = now.astimezone(utc_8)

split = str(time_now).split(" ")
print(split[0])
split = split[1].split(":")
print((split[0]+split[1]))





