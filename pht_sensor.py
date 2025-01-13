import board
from adafruit_ms8607 import MS8607
import displayio
import terminalio
import time
from adafruit_st7789 import ST7789
from adafruit_display_text import label

#variables
i2c = board.I2C()
pht = MS8607(i2c)

print(pht.pressure)
pressure_str = str(pht.pressure) + " hPa "

print(pht.relative_humidity)
humidity = (int(pht.relative_humidity * 100)) / 100
humidity_str = str(humidity) + "% "

farenh = (9/5) * pht.temperature + 32
farenh = (int(farenh * 100)) / 100
farenh_str = str(farenh) + " deg F"
print(farenh_str)


#display content
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D3
tft_dc = board.D4
dbus = displayio.FourWire(spi, command = tft_dc, chip_select = tft_cs)
display = ST7789(dbus, rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)
screen = displayio.Group()
display.root_group = screen 
my_bitmap = displayio.Bitmap(240, 135, 1)

#word
pressW = pressure_str + " hPa"
text_color = 0xFF69B4
FONTSCALE = 2
text_area = label.Label(terminalio.FONT, text=pressW, color=text_color)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(scale=FONTSCALE, x=60, y=70)
text_group.append(text_area)
screen.append(text_group)

temps = [pressure_str, humidity_str, farenh_str]

while True:
    for temp in temps:
        text_area.text = temp
        time.sleep(3)
