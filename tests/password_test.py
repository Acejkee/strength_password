from strength_password import strength_password
import pytest


@pytest.mark.parametrize("value , expected_result", [('1234567', "В Вашем пароле меньше 8 символов!"),
                                                      ('qwerty', "В Вашем пароле меньше 8 символов!"),
                                                      ('QWERTY', "В Вашем пароле меньше 8 символов!"),
                                                      ('aWrsa77', "В Вашем пароле меньше 8 символов!"),
                                                      ('WWWW85', "В Вашем пароле меньше 8 символов!")])
def test_password_len(value , expected_result):
    assert strength_password(value) == expected_result


@pytest.mark.parametrize("value , expected_result", [('12345678', "Ваш пароль недостаточно надежен, попробуйте добавить цифры, заглавные и строчные буквы!"),
                                                      ('qwertyqwerty', "Ваш пароль недостаточно надежен, попробуйте добавить цифры, заглавные и строчные буквы!"),
                                                      ('QWERTYASDASD', "Ваш пароль недостаточно надежен, попробуйте добавить цифры, заглавные и строчные буквы!")])
def test_password_only_one_types(value, expected_result):
    assert strength_password(value) == expected_result


@pytest.mark.parametrize("value , expected_result", [('1234qwer', "Ваш пароль хороший, но Вы можете его улучшить, пароль должен состоять из цифр, заглавых и строчных букв"),
                                                      ('qwertyQWERR', "Ваш пароль хороший, но Вы можете его улучшить, пароль должен состоять из цифр, заглавых и строчных букв"),
                                                      ('QWERTY1233', "Ваш пароль хороший, но Вы можете его улучшить, пароль должен состоять из цифр, заглавых и строчных букв")])
def test_password_two_types(value, expected_result):
    assert strength_password(value) == expected_result


@pytest.mark.parametrize("value , expected_result", [('1234qwerQWEQE', "Ваш пароль достаточно надежен!"),
                                                      ('wqe21312R', "Ваш пароль достаточно надежен!"),
                                                      ('QQWEQWEA3d', "Ваш пароль достаточно надежен!")])
def test_password_correct(value, expected_result):
    assert strength_password(value) == expected_result


if __name__ == '__main__':
    pytest.main()
