#!/usr/bin/env python3
from datetime import datetime, time, timedelta

LCD_WIDTH = 16

def center_print(text):
    print(text.center(LCD_WIDTH))

current_time = datetime.now()
today = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
sleep_time = today + timedelta(hours=21, minutes=30)
wakeup_time = sleep_time + timedelta(hours=8, minutes=30)

if current_time < sleep_time:
    delta = (sleep_time - current_time)
    center_print("Time to sleep")
    center_print("{}h {}m".format(delta.seconds//3600, (delta.seconds//60)%60))
else:
    delta = (wakeup_time - current_time)
    center_print("Time to wake up")
    center_print("{}h {}m".format(delta.seconds//3600, (delta.seconds//60)%60))

