import string
import random
import math


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def string_generator(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def number_generator(length):
    digits = "1234567890"
    code = ""

    for i in range(length):
        code += digits[math.floor(random.random() * 10)]
    return code
