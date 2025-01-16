import board
from adafruit_ms8607 import MS8607
import displayio
import terminalio
import time
from adafruit_st7789 import ST7789
from adafruit_display_text import label
from adafruit_ds3231 import DS3231

#variables
i2c = board.I2C()
pht = MS8607(i2c)
rtc = DS3231(i2c)

INTERVAL1 = 3
INTERVAL2 = 5

#main program
curr_time1 = time.monotonic()
curr_time2 = curr_time1


while True:
    if time.monotonic() - curr_time1 >= INTERVAL1:
        curr_time1 = time.monotonic()
        date_time = '{:0>2}/{:0>2}/{:0>2} {:0>2}:{:0>2}'.format(rtc.datetime[1], rtc.datetime[2], rtc.datetime[0]%100, rtc.datetime[3], rtc.datetime[4])
        print(date_time)
    if time.monotonic() - curr_time2 >= INTERVAL2:
        curr_time2 = time.monotonic()
        print(f'Pressure {pht.temperature:.2f} hPa')
        print(f'Temperature {(pht.temperature * 9 /5 + 32):.2f} def F')
        print(f'Humidity {pht.relative_humidity:.2f}%')
        
