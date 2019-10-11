#!/usr/bin/env python3
from datetime import date, datetime

start_date = date(2019, 10, 8)
start_page = 260
pages_per_day = 2

today_date = datetime.now().date()
days_from_start = (today_date - start_date).days
expected_page_today = start_page + days_from_start * pages_per_day

print("Stallings:\n{}: {}".format(today_date, expected_page_today))
