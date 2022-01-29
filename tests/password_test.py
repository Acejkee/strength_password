from strength_password import strength_password
import pytest


@pytest.mark.parametrize("value , expected_result" , [('1234567', "В Вашем пароле меньше 8 символов!"),
                                                      ('qwerty', "В Вашем пароле меньше 8 символов!"),
                                                      ('QWERTY', "В Вашем пароле меньше 8 символов!"),
                                                      ('aWrsa77', "В Вашем пароле меньше 8 символов!"),
                                                      ('WWWW85', "В Вашем пароле меньше 8 символов!")])
def test_password_len(value , expected_result):
    assert strength_password(value) == expected_result


if __name__ == '__main__':
    pytest.main()
