import random
import string


def generate_password(length=10):

    chars = (
        string.ascii_letters +
        string.digits +
        "@#$%"
    )

    return ''.join(
        random.choice(chars)
        for _ in range(length)
    )


def generate_username(name):

    first = (
        name.split()[0]
        .upper()
    )

    random_number = random.randint(
        100,
        999
    )

    return f"{first}{random_number}"