#!/usr/bin/env python3
import argparse
import os
import subprocess
from time import sleep
from RPLCD.gpio import CharLCD
from RPi import GPIO

def lcd_write(text):
    text = text.replace('\n', '\n\r')
    lcd = CharLCD(
            pin_rs=15, pin_rw=16, pin_e=18,
            pins_data=[21, 22, 23, 24],
            numbering_mode=GPIO.BOARD,
            cols=16, rows=2, dotsize=8,
            charmap='A02',
            auto_linebreaks=True
          )

    lcd.clear()
    lcd.write_string(text)

if __name__ == '__main__':
    lcd_write("Test message")

