import adafruit_ssd1306
import board
import busio
import digitalio
import time

from PIL import Image, ImageDraw, ImageFont

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
        self.oled.fill(0)
        self.oled.show()

        self.image = self.get_image(0)

    def get_image(self, off):
        image = Image.new("1", (self.oled.width, self.oled.height))

        draw = ImageDraw.Draw(image)

        draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=0)

        font = ImageFont.load_default()
        text = "Hello World!"
        draw.text(
            (off, 0),
            text,
            font=font,
            fill=255,
        )
        return image

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def run_once(self):
        _step_len = 2
        _step = int(self.step // _step_len)
        if self.step % _step_len == 0:
            print(_step)
            _off = _step % 40
            print(_off)
            self.image = self.get_image(_off)
            self.oled.image(self.image)
            self.oled.show()

    def run(self):
        while True:
            self.run_once()
            time.sleep(0.1)
            self.step += 1


