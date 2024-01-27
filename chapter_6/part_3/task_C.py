# Суммирование ответов 2
# Сервер отвечает на запрос JSON списком.
# Выведите сумму чисел в полученном списке.
#
# Формат ввода
# Вводится адрес сервера
#
# Формат вывода
# Одно число — сумма всех чисел в полученном списке.
from requests import get

url = input()
numbers = get(f'http://{url}').json()
numbers_sum = sum(number for number in numbers if isinstance(number, int))

print(numbers_sum)
