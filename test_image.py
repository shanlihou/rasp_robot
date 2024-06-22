from PIL import Image, ImageSequence


img = Image.open('a.gif')

frames = [frame.copy() for frame in ImageSequence.Iterator(img)]


for frame in frames:
    print(type(frame))
    frame = frame.resize((128, 64))
    print(frame.size)
