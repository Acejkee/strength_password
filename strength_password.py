import string


def strength_password(value: str) -> str:
    if len(value) < 8:
        return "В Вашем пароле меньше 8 символов!"
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue
    if count == 3:
        return "Ваш пароль достаточно надежен!"
    return "Ваш пароль недостаточно надежен, попробуйте добавить цифры, заглавные и строчные буквы!" if count == 1 \
        else "Ваш пароль хороший, но Вы можете его улучшить, пароль должен состоять из цифр, заглавых и строчных букв"


if __name__ == '__main__':
    print(strength_password('123'))
