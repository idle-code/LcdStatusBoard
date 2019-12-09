#!/usr/bin/env python3
from datetime import datetime, time, timedelta

DISPLAY_WIDTH = 16

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

today = current_time.replace(hour=0, minute=0, second=0, microsecond=0)

work_start = today.replace(hour=10, minute=0)
work_duration = timedelta(hours=7)
work_end = work_start + work_duration


if current_time < work_start:
    print("Work starts at:")
    print("{:%H:%M}".format(work_start).center(DISPLAY_WIDTH))
elif current_time > work_end:
    print("Work ended at:")
    print("{:%H:%M}".format(work_end).center(DISPLAY_WIDTH))
else:
    work_left_seconds = (work_end - current_time).total_seconds()
    work_left_hours = work_left_seconds // (60*60)
    work_left_minutes = (work_left_seconds % (60*60)) / 60
    print("Left: {:0.0f}:{:0.0f}".format(work_left_hours, work_left_minutes))

    pb = ProgressBar(1 - (work_left_seconds / work_duration.total_seconds()))
    print(pb)

