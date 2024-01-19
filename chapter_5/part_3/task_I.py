# Валидация пользователя
# Используйте две предыдущих функции валидации и напишите функцию user_validation,
# которая принимает именованные аргументы:
#
# last_name — фамилия;
# first_name — имя;
# username — имя пользователя.
# Если функции был передан неизвестный параметр или не передан один из обязательных, то вызовите исключение KeyError.
#
# Если один из параметров не является строкой, то вызовите исключение TypeError.
#
# Обработка данных должна происходить в порядке: фамилия, имя, имя пользователя.
#
# Если поле заполнено верно, функция возвращает словарь с данными пользователя.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.
import string


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not all(letter in string.digits + string.ascii_letters + '_' for letter in name):
        raise BadCharacterError
    if name[0].isdigit():
        raise StartsWithDigitError
    return name


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not all(ord('а') <= ord(letter.lower()) <= ord('ё') for letter in name):
        raise CyrillicError
    if name != name.lower().capitalize():
        raise CapitalError
    return name


def user_validation(**kwargs):
    if kwargs.keys() != {'last_name', 'first_name', 'username'}:
        raise KeyError
    if any(not isinstance(value, str) for value in kwargs.values()):
        raise TypeError
    name_validation(kwargs['last_name'])
    name_validation(kwargs['first_name'])
    username_validation(kwargs['username'])
    return kwargs
