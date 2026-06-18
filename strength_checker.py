import string


def check_strength(password):

    score = 0
    reasons = []

    if len(password) >= 12:
        score += 1
    else:
        reasons.append("Password is too short")

    if any(char.isupper() for char in password):
        score += 1
    else:
        reasons.append("No uppercase letters")

    if any(char.islower() for char in password):
        score += 1
    else:
        reasons.append("No lowercase letters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        reasons.append("No numbers")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        reasons.append("No symbols")

    if score <= 2:
        strength = "Weak 🔴"

    elif score <= 4:
        strength = "Medium 🟡"

    else:
        strength = "Strong 🟢"

    return strength, reasons