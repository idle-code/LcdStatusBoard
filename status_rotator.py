#!/usr/bin/env python3
import argparse
import os
import subprocess
from time import sleep
from RPLCD.gpio import CharLCD
from RPi import GPIO

LCD_COLS = 16

def lcd_write(text, delay=3, scroll_delay=0.2):
    if not text:
        return

    lcd = CharLCD(
            pin_rs=15, pin_rw=16, pin_e=18,
            pins_data=[21, 22, 23, 24],
            numbering_mode=GPIO.BOARD,
            cols=LCD_COLS+1, rows=2, dotsize=8,
            charmap='A02',
            auto_linebreaks=False
          )

    text_lines = list(filter(None, text.split('\n')))[-2:]
    if len(text_lines) != 2:
        text_lines.append("")
    assert len(text_lines) == 2

    longest_line_len = max(map(len, text_lines))

    animation_length = 1 + max(0, longest_line_len - LCD_COLS)
    lcd.clear()
    for frame, offset in enumerate(range(animation_length)):
        for line in text_lines:
            line = line[offset:offset+LCD_COLS].ljust(LCD_COLS)
            assert len(line) == LCD_COLS
            lcd.cursor_pos = (lcd.cursor_pos[0], 0)
            lcd.write_string(line)
            lcd.crlf()

        if frame == 0 or (animation_length > 1 and frame == animation_length-1):
            # Wait longer on first and last frame
            sleep(delay)
        else:
            sleep(scroll_delay)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LCD text rotation utility")
    parser.add_argument('-d', '--delay', type=float, default=3.0, help="Delay between different messages in seconds")
    parser.add_argument('-s', '--scroll-delay', type=float, default=0.3, help="Animation delay of scrolling message in seconds seconds")
    parser.add_argument('directory', type=str, help="Path to the directory with messages")

    args = parser.parse_args()
    delay_seconds = args.delay
    scroll_delay_seconds = args.scroll_delay
    directory_path = args.directory
    
    delay_seconds = max(delay_seconds, .3)
    
    if not os.path.isdir(directory_path):
        print("{} is not a directory".format(directory_path))
        exit(1)
    
    while True:
        message_files = sorted(os.listdir(directory_path))
        message_files = map(lambda file_path: os.path.join(directory_path, file_path), message_files)
        message_files = list(filter(os.path.isfile, message_files))
        if len(message_files) == 0:
            print("There is no files in message directory")
            sleep(delay_seconds)
            continue 

        print("There are {} files in watched directory".format(len(message_files)))
        for f in message_files:
            message = ''
            try:
                if os.access(f, os.X_OK):
                    print("Executing " + f)
                    process_info = subprocess.run(f, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
                    message = process_info.stdout
                else:    
                    print("Displaying " + f)
                    with open(f, 'r') as message_file:
                        message = message_file.read()
            except FileNotFoundError:
                print("{} file not found - skipping".format(f))

            lcd_write(message, delay_seconds, scroll_delay_seconds)

