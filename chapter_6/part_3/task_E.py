# Суммирование ответов 3
# Сервер отвечает на несколько путей, каждый из которых возвращает свой JSON список.
# Напишите программу, которая произведёт сбор и суммирование всех данных по заданным путям.
#
# Формат ввода
# Вводится адрес сервера и список анализируемых путей.
#
# Формат вывода
# Одно число — сумма всех чисел из полученных списков.
from requests import get
from sys import stdin

url = input()
paths = [path.strip() for path in stdin]
numbers_sum = 0

for path in paths:
    response = get(f'http://{url}{path}')
    numbers = response.json()
    numbers_sum += sum(numbers)

print(numbers_sum)
