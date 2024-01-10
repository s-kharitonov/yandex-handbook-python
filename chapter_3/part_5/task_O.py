# Поставь себя на моё место
# Вы уже долгое время решаете задачи в Яндекс.Контесте.
# Сегодня пришло время почувствовать себя на его месте.
#
# Напишите небольшой кусочек тестирующей системы.
#
# Вашему решению доступен файл scoring.json, в котором содержится информация о системе проверки.
#
# Основой системы является список групп тестов.
# Каждая группа представляет собой объект с полями:
#
# points — количество очков, которое можно получить за прохождение данной группы;
# tests — список объектов с описанием конкретного теста.
# Объект описывающий тест содержит поля:
#
# input — строка входных данных теста;
# pattern — строка ожидаемых в качестве ответа.
# В стандартный поток ввода вашего решения передаются ответы, полученные от тестируемой программы.
#
# Формат ввода
# В стандартный поток ввода передаются строки — ответы тестируемой программы на каждый тест.
# В файле scoring.json содержится информация о тестах задачи.
#
# Формат вывода
# Одно число — количество полученных тестируемой программой баллов.
# Если группа тестов не была пройдена полностью, то за данную группу ставится пропорциональный балл.
# Гарантируется, что баллы за группу кратны количеству тестов в ней.
from sys import stdin
import json

with open('scoring.json', 'r', encoding='UTF-8') as scoring_file:
    scoring = json.load(scoring_file)
    user_answers = stdin.readlines()
    current_answer = 0
    result = 0

    for scoring_element in scoring:
        points = scoring_element['points']
        tests = scoring_element['tests']
        points_per_test = points // len(tests)

        for test in tests:
            user_answer = user_answers[current_answer].rstrip('\n')

            if user_answer == test['pattern']:
                result += points_per_test

            current_answer += 1

    print(result)
