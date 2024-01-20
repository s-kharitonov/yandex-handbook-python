# Валидация пароля
# После того как пользователь ввёл свои данные в требуемом формате, можно позаботиться и о пароле.
#
# Напишите функцию password_validation, которая принимает один позиционный параметр — пароль,
# и следующие именованные параметры:
#
# min_length — минимальная длина пароля, по умолчанию 8;
# possible_chars — строка символов, которые могут быть в пароле, по умолчанию латинские буквы и цифры;
# at_least_one — функция возвращающая логическое значение, по умолчанию str.isdigit.
# Если переданный позиционный параметр не является строкой, вызовите исключение TypeError.
#
# А так же реализуйте собственные исключения:
#
# MinLengthError — вызывается, если пароль меньше заданной длины;
# PossibleCharError — вызывается, если в пароле используется недопустимый символ;
# NeedCharError — вызывается, если в пароле не найдено ни одного обязательного символа.
# Проверка условий должна происходить в порядке указанном в задании.
#
# Так как, хороший разработчик никогда не хранит пароли в открытом виде, функция, в случае успешного завершения,
# возвращает хеш пароля. Для этого воспользуйтесь функцией sha256 из пакета hashlib
# и верните его шестнадцатеричное представление.
import string
from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8, possible_chars=string.ascii_letters + string.digits,
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if any(letter not in possible_chars for letter in password):
        raise PossibleCharError
    if not any(map(at_least_one, password)):
        raise NeedCharError
    return sha256(password.encode()).hexdigest()
