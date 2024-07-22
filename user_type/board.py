import adafruit_ssd1306
import board
import busio
import digitalio
import time

from ctrl import gif_ctrl
from ctrl import text_ctrl
from PIL import Image, ImageDraw, ImageFont, ImageSequence

from common import const


class Board(object):
    def __init__(self) -> None:
        self.step = 0
# SPI初始化
# pin脚信息在board库里，是BCM模式
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        reset_pin = digitalio.DigitalInOut(board.D17)
        dc_pin = digitalio.DigitalInOut(board.D22)
        cs_pin = digitalio.DigitalInOut(board.CE0)

        self.oled = adafruit_ssd1306.SSD1306_SPI(const.WIDTH, const.HEIGHT, spi, dc_pin, reset_pin, cs_pin)
# 初始化 清除屏幕信息
        self.clear()

        self._ctrl = text_ctrl.TextController(self.oled.width, self.oled.height)

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def run_once(self):
        self.oled.image(self._ctrl.next_frame())
        self.oled.show()

    def run(self):
        while True:
            self.run_once()
            time.sleep(0.1)
            self.step += 1


