# Валидация имени пользователя
# Продолжим реализацию системы валидации.
#
# Напишите функцию username_validation, которая принимает один позиционный аргумент — имя пользователя:
#
# Если параметр не является строкой, то вызовите исключение TypeError.
#
# А также разработайте собственные ошибки:
#
# BadCharacterError — вызывается, если значение состоит не только из латинских букв,
# цифр и символа нижнего подчёркивания;
# StartsWithDigitError — вызывается, если значение начинается с цифры.
# Обработка ошибок должна происходить в порядке, указанном в задании.
#
# В случае успешного выполнения, функция должна вернуть переданный параметр без изменений.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.
import string


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name):
    if not isinstance(name, str):
        raise TypeError
    if not all(letter in string.digits + string.ascii_letters + '_' for letter in name):
        raise BadCharacterError
    if name[0].isdigit():
        raise StartsWithDigitError
    return name
