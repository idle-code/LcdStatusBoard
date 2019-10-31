#!/usr/bin/env python3
from datetime import date, datetime

def calculate_progress(start_date, start_page, pages_per_day):
    today_date = datetime.now().date()
    days_from_start = (today_date - start_date).days
    expected_page_today = start_page + days_from_start * pages_per_day
    return expected_page_today


start_date = date(2019, 10, 8)
start_page = 260
pages_per_day = 2

stalling_page_today = calculate_progress(
            start_date = date(2019, 10, 8),
            start_page = 260,
            pages_per_day = 2
        )
print("Stallings: {}".format(stalling_page_today))

pragmatic_page_today = calculate_progress(
            start_date = date(2019, 10, 15),
            start_page = 216,
            pages_per_day = 2
        )
print("Pragmatic: {}".format(pragmatic_page_today))
