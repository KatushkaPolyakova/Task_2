import random
import string


def generate_user():
    return {        
        'email': ''.join(random.choice(string.ascii_lowercase) for _ in range(10))+ '@mail.ru',
        'password':''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
        'name': ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
        }


