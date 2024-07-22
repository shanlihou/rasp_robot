import os
import re
from PIL import Image, ImageDraw, ImageFont, ImageSequence

class TextController(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = ImageFont.load_default()


    def get_image(self, off):
        image = Image.new("1", (self.width, self.height))

        draw = ImageDraw.Draw(image)

        draw.rectangle((0, 0, self.width, self.height), outline=255, fill=0)

        text = "Hello World!"
        draw.text(
            (off, 0),
            text,
            font=self.font,
            fill=255,
        )
        return image

    def get_ip_info(self):
        _pat = re.compile(r'inet\s+([0-9.]+)\s+netmask\s+([0-9.]+)\s+broadcast\s+([0-9.]+)')
        with os.popen('ifconfig') as f:
            _data = f.read()
            print(_data)
            _find = _pat.findall(_data)
            print(_find)
            return _data

    def next_frame(self):
        self.get_ip_info()
        return self.get_image(0)