# Список пользователей
# На сервере по пути /users, доступен список пользователей, представленных JSON объектами с ключами:
#
# id — уникальный идентификатор пользователя;
# username — имя пользователя;
# last_name — фамилия;
# first_name — имя;
# email — адрес электронной почты.
# Формат ввода
# В первой строке вводится адрес сервера.
#
# Формат вывода
# Выведите список всех пользователей системы в алфавитном порядке.
from requests import get

url = input()
response = get(f'http://{url}/users')
users = sorted(map(lambda user: f'{user["last_name"]} {user["first_name"]}', response.json()))

print(*users, sep='\n')
