# Слияние данных
# Одна местная компания производит обновление данных о пользователях и заодно решили реорганизовать систему хранения.
#
# Напишите программу, которая обновляет данные о пользователях, записанных в JSON файле.
#
# Формат ввода
# Пользователь вводит два имени файла.
# В первом хранится JSON массив пользователей.
# Во втором — массив новых данных.
#
# Информация о каждом пользователе представляется JSON объектом,
# в котором обязательно присутствует поле name, описывающее имя пользователя. Остальные поля являются дополнительными.
#
# Формат вывода
# В первый файл запишите информацию о пользователях в виде JSON объекта, ключами которого выступают имена пользователей,
# а значениями — объекты с информацией о них.
#
# Если какая-либо дополнительная информация о пользователе изменяется,
# то требуется сохранить лексикографически большее значение.
import json

users_file_name = input()
additional_info_file_name = input()

with open(users_file_name, 'r', encoding='UTF-8') as users_file:
    users = json.load(users_file)
with open(additional_info_file_name, 'r', encoding='UTF-8') as additional_info_file:
    additional_info = json.load(additional_info_file)
with open(users_file_name, 'w', encoding='UTF-8') as result_file:
    users_by_name = {user['name']: {key: value for key, value in user.items() if key != 'name'} for user in users}
    info_by_username = {info['name']: info for info in additional_info}

    for info in additional_info:
        username = info['name']
        user = users_by_name[username]

        for key, value in info.items():
            if key == 'name':
                continue
            if key not in user:
                user[key] = value
                continue
            if user[key] < value:
                user[key] = value

    json.dump(users_by_name, result_file, ensure_ascii=False)
