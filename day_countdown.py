#!/usr/bin/env python3
from datetime import datetime, time, timedelta

DISPLAY_WIDTH = 16
START_DATE_STR = '2021-08-03'
END_DATE_STR = '2021-10-01'

class ProgressBar:
    def __init__(self, value=0):
        self.width = DISPLAY_WIDTH
        self.value = value
        self.fill_char = '#'
        self.empty_char = ' '

    @property
    def value(self) -> float:
        return self.position / self.width

    @value.setter
    def value(self, percentage: float):
        self.position = round(percentage * self.width)

    def __str__(self):
        return self.fill_char * self.position + self.empty_char * (self.width - self.position)


current_time = datetime.now()

start_date = datetime.strptime(START_DATE_STR, '%Y-%m-%d') 
end_date = datetime.strptime(END_DATE_STR, '%Y-%m-%d')
duration = end_date - start_date


if current_time < start_date:
    print("Timer starts at")
    print(start_date.isoformat().center(DISPLAY_WIDTH))
elif current_time > end_date:
    print("Timer ended at")
    print(end_date.isoformat().center(DISPLAY_WIDTH))
else:
    left_seconds = (end_date - current_time).total_seconds()
    left_days = left_seconds // (60*60*24)
    left_hours = (left_seconds % (60*60*24)) // (60*60)
    print("Left: {:0.0f}d {:0.0f}h".format(left_days, left_hours))

    pb = ProgressBar(1 - (left_seconds / duration.total_seconds()))
    print(pb)

