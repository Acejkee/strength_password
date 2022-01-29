import string


def strength_password(value: str) -> str:
    digits = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    if len(value) < 8:
        return "В Вашем пароле меньше 8 символов!"
    if all(e in digits for e in value) or all(e in lower for e in value) or all(e in upper for e in value):
        return "Ваш пароль недостаточно надежен, попробуйте добавить цифры, заглавные и строчные буквы!"
    if any(e in digits for e in value) and any(e in lower for e in value) and any(e in upper for e in value):
        return "Ваш пароль достаточно надежен!"
    if (any(e in digits for e in value) and any(e in lower for e in value)) or (any(e in digits for e in value)
                                                                                and any(e in upper for e in value)) or (
            any(e in lower for e in value) and any(e in upper for e in value)):
        return "Ваш пароль хороший, но Вы можете его улучшить, пароль должен состоять из цифр, заглавых и строчных букв"


if __name__ == '__main__':
    print(strength_password('123'))
