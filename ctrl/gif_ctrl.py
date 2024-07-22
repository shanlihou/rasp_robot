
from PIL import Image, ImageDraw, ImageFont, ImageSequence


class GifController(object):
    def __init__(self, gif_path):
        self._frames = self._load_image(gif_path)
        self._idx = 0
        
    def _load_image(self, path):
        img = Image.open(path)
        frames = []
        for frame in ImageSequence.Iterator(img):
            frame = frame.resize((128, 64))
            frame = frame.convert("1")

            frames.append(frame)
            print(id(frame))
            print(len(frames))

        return frames

    def next_frame(self):
        _frame = self._frames[self._idx]
        self._idx += 1
        if self._idx >= len(self._frames):
            self._idx = 0

        return _frame


