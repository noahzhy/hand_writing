# hard_writing_test.py
# coding: utf-8
from PIL import Image, ImageFont

from handright import Template, handwrite

text = """



"""
template = Template(
    background=Image.new(
        mode="1",
        size=(2480, 3508),
        color=1,

    ),
    line_spacing=100,
    left_margin=100,
    top_margin=100,
    right_margin=100,
    bottom_margin=100,
    word_spacing=10,
    font=ImageFont.truetype("00002.ttf", size=80),
)
images = handwrite(text, template)
for idx, im in enumerate(images):
    assert isinstance(im, Image.Image)
    # im.show()
    im.save("ex{:04d}.png".format(idx))
