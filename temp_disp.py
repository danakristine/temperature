#importsss
import board
import displayio
import terminalio
import time
from analogio import AnalogIn
from adafruit_st7789 import ST7789
from adafruit_display_text import label


#values
pot = AnalogIn(board.A0)
volt = (pot.value / 65535 * 3.3)
temp = (volt - 0.5) * 100
farenh = (9/5) * temp + 32
farenh = (int(farenh * 100)) / 100
farenh_str = str(farenh)
print(farenh_str)

#display content
background_color = 0xFADADD
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D3
tft_dc = board.D4
dbus = displayio.FourWire(spi, command = tft_dc, chip_select = tft_cs)
display = ST7789(dbus, rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)
screen = displayio.Group()
display.root_group = screen 
my_bitmap = displayio.Bitmap(240, 135, 1)
my_palette = displayio.Palette(1)
my_palette[0] = background_color
tile_grid = displayio.TileGrid(my_bitmap, pixel_shader = my_palette, x = 0, y = 0)
screen.append(tile_grid)

#word
tempW = farenh_str + " deg F"
text_color = 0xFF69B4
FONTSCALE = 2
text_area = label.Label(terminalio.FONT, text=tempW, color=text_color)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(scale=FONTSCALE, x=60, y=70)
text_group.append(text_area)
screen.append(text_group)


#main
while True:
    volt = (pot.value / 65535 * 3.3)
    temp = (volt - 0.5) * 100
    farenh = (9/5) * temp + 32
    farenh = (int(farenh * 100)) / 100
    farenh_str = str(farenh)
    print(farenh_str)
    
    text_area.text = farenh_str + " deg F"
    time.sleep(5)
