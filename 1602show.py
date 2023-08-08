from machine import SoftI2C,Pin
from lcd_i2c import LCD
import time

i2c = SoftI2C(scl=Pin(15),sda=Pin(13),freq=100000)
lcd = LCD(addr=i2c.scan()[0], cols=16, rows=2, i2c=i2c)

lcd.begin()
lcd.print("hello! mcu")

time.sleep(1)
for i in range(1,101):
    lcd.clear()
    lcd.print(f"{i}")
    time.sleep(1)

