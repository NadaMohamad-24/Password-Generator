import string
import secrets
import random


def generate_password(length, uppercase, lowercase, numbers, symbols):

    password = []

    all_characters = ""

    if uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
        all_characters += string.ascii_uppercase

    if lowercase:
        password.append(secrets.choice(string.ascii_lowercase))
        all_characters += string.ascii_lowercase

    if numbers:
        password.append(secrets.choice(string.digits))
        all_characters += string.digits

    if symbols:
        password.append(secrets.choice(string.punctuation))
        all_characters += string.punctuation

    if not all_characters:
        return ""

    while len(password) < length:
        password.append(secrets.choice(all_characters))

    random.shuffle(password)

    return "".join(password)