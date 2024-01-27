# Удаление данных
# Завершим эпопею с сервером из прошлых задач.
# При DELETE запросе по пути /users/<id> производится удаление пользователя с заданным идентификатором.
#
# Напишите программу, которая удаляет пользователя из системы.
#
# Формат ввода
# В первой строке вводится адрес сервера.
# Во второй строке записан идентификатор пользователя, информацию о котором требуется удалить.
#
# Формат вывода
# Ничего выводить не требуется.
from requests import delete

url = input()
user_id = input()

delete(f'http://{url}/users/{user_id}')
