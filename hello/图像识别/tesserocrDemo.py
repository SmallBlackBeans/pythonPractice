# coding: utf-8

import tesserocr
from PIL import Image
image = Image.open('xxx.png')
print(tesserocr.image_to_text(image))


print(tesserocr.file_to_text('xxx.png'))