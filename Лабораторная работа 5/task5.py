from string import digits, ascii_uppercase, ascii_lowercase
import random


def get_random_password(num=8) -> str:
    str_ = digits + ascii_uppercase + ascii_lowercase
    password = ''.join(random.sample(str_, num))

    return password


print(get_random_password())
