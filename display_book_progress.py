#!/usr/bin/env python3
from RPLCD.gpio import CharLCD
from RPi import GPIO
from datetime import date, datetime

def lcd_write(text):
    lcd = CharLCD(
            pin_rs=15, pin_rw=16, pin_e=18,
            pins_data=[21, 22, 23, 24],
            numbering_mode=GPIO.BOARD,
            cols=20, rows=4, dotsize=8,
            charmap='A02',
            auto_linebreaks=True
          )

    lcd.clear()
    lcd.write_string(text)

start_date = date(2019, 10, 8)
start_page = 280
pages_per_day = 2

today_date = datetime.now().date()
days_from_start = (today_date - start_date).days
expected_page_today = start_page + days_from_start * pages_per_day

lcd_write("Stallings:\n\r{}: {}".format(today_date, expected_page_today))
