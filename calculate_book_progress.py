#!/usr/bin/env python3
from datetime import date, datetime, timedelta
from collections import namedtuple

Book = namedtuple('Book', 'name total_pages')

class BookProgress:
    def __init__(self, book: Book, start_date: date, start_page: int = 0, pages_per_day: int = 2):
        self.book = book
        self.start_date = start_date
        self.start_page = start_page
        self.pages_per_day = pages_per_day
        self.end_date = start_date + timedelta(days=(self.book.total_pages - self.start_page) // self.pages_per_day)

    def _calculate_progress(self):
        today_date = datetime.now().date()
        days_from_start = (today_date - self.start_date).days
        expected_page_today = self.start_page + days_from_start * self.pages_per_day
        days_left = (self.end_date - today_date).days
        return expected_page_today, days_left

    def __str__(self):
        page_today, days_left = self._calculate_progress()
        progress_fraction = page_today / self.book.total_pages
        first_line = "{}: p{}".format(self.book.name, page_today)
        if days_left > 0:
            #second_line = "\nEnds in {} days ({})".format(days_left, self.end_date)
            second_line = "{:.0%} | {}d left".format(progress_fraction, days_left)
        elif days_left == 0:
            second_line = "Ends today"
        else:
            second_line = "Ended {} days ago".format(-days_left)

        return first_line + "\n" + second_line


stallings = Book(name='Stallings', total_pages=818)
stallings_progress = BookProgress(
        stallings,
        start_date = date(2019, 10, 8),
        start_page = 260,
        pages_per_day = 2)

print(stallings_progress)

