import random
import string

def generate_email(first_name="test", last_name="user", cohort=19, suffix_length=3):
    """
    Генерирует email для регистрации.
    Формат: имя_фамилия_номер_когорты_любые_3_цифры@yandex.ru
    """
    suffix = ''.join(random.choices(string.digits, k=suffix_length))
    return f"{first_name}_{last_name}_{cohort}_{suffix}@yandex.ru"

def generate_password(length=8):
    """Генерирует случайный пароль заданной длины."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
