# А роза упала на лапу Азора 7.0
# Напишите функцию is_palindrome, которая принимает натуральное число, строку, кортеж или список,
# а возвращает логическое значение: True — если передан палиндром, а в противном случае — False.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
#
# Для определения типа параметра можно воспользоваться функцией type или более продвинутой isinstance

def is_palindrome(value):
    if isinstance(value, int):
        reversed_number = 0
        number = value

        while number > 0:
            last_digit = number % 10
            number //= 10
            reversed_number *= 10
            reversed_number += last_digit

        return reversed_number == value
    else:
        for i, element in enumerate(value):
            element_pair = value[-i - 1]
            if element_pair != element:
                return False

        return True

