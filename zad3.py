import random
import string
from english_words import get_english_words_set


def is_password_contain_word(password):
    for word in get_english_words_set(['web2']):
        if word in password and len(word) > 1:
            return True
    return False


def generate_password():
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
        if any(p.islower() for p in password) \
                and any(p.isupper() for p in password) \
                and any(p in string.punctuation for p in password) \
                and any(p.isdigit() for p in password) \
                and is_password_contain_word(password):
            break
    return password


print(f'Password {generate_password()}')
