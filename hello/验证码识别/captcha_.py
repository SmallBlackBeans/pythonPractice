from captcha.image import ImageCaptcha
from PIL import Image
import numpy as np # 科学计算




VOCAB = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CAPTCHAR_LENGTH = 4
VOCAB_LENGTH = len(VOCAB)


def generate_captcha(captcha_text):
    """
    把验证码转化成了每个像素的 RGB
    :param captcha_text:
    :return:
    """
    image = ImageCaptcha()
    captcha = image.generate(captcha_text)
    captcha_image = Image.open(captcha)
    captcha_array = np.array(captcha_image)
    return captcha_array
