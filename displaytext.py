from PIL import ImageFont

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import  sh1106
from time import sleep

# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
serial = i2c(port=1, address=0x3C)

# substitute ssd1331(...) or sh1106(...) below if using that device
device = sh1106(serial)
font = ImageFont.truetype("arial.ttf", 20)

with canvas(device) as draw:
    draw.text((0,0), "hello", fill="white")
    draw.text(xy=(0,20),text= "xin chào được viết ", fill="white", font=font)
sleep(5)
