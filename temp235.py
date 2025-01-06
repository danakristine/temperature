#imports
import board
import time
from analogio import AnalogIn


#values
pot = AnalogIn(board.A0)

while True:
    volt = (pot.value / 65535 * 3.3)
    temp = (volt - 0.5) * 100
    farenh = (9/5) * temp + 32
    print(farenh)
    time.sleep(0.6)
