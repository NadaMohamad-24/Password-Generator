import json
import os


FILE_NAME = "password_history.json"


def save_password(password):

    passwords = []

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            try:
                passwords = json.load(file)

            except:
                passwords = []

    passwords.append(password)

    with open(FILE_NAME, "w") as file:

        json.dump(passwords, file, indent=4)


def load_passwords():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            try:
                return json.load(file)

            except:
                return []

    return []