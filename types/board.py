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

# 创建一个空白的图像
# 确保用“1”表示 1bit 的颜色
        image = Image.new("1", (self.oled.width, self.oled.height))

# 获取绘制对象来绘制图像
        draw = ImageDraw.Draw(image)

# 绘制一个白色的背景
        draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)

# 绘制一个小的内边框
        draw.rectangle(
            (
                const.BORDER, 
                const.BORDER, 
                self.oled.width - const.BORDER - 1, 
                self.oled.height - const.BORDER - 1
            ), 
            fill=0, 
            outline=0)

# 加载默认样式
        font = ImageFont.load_default()
# 绘制一些文字
        text = "Hello World!"
#(font_width, font_height) = font.getsize(text)
        draw.text(
            (0, 0),
            text,
            font=font,
            fill=255,
        )

        self.image = image

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def run_once(self):
        if self.step % 30 == 0:
            self.oled.image(self.image)
            self.oled.show()

    def run(self):
        while True:
            self.run_once()
            time.sleep(0.1)
            self.step += 1


