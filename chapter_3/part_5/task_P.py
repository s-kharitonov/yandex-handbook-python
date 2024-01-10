# Найдётся всё 3.0
# Давайте вновь напишем небольшой компонент поисковой системы.
#
# Формат ввода
# Сначала вводится поисковый запрос.
# Затем вводятся имена файлов, среди которых следует произвести поиск.
#
# Формат вывода
# Выведите все имена файлов, в которых есть поисковая строка без учета регистра и повторяющихся пробельных символов.
# Если ни в одном файле информация не была найдена, выведите "404. Not Found".
#
# Примечание
# Система поиска должна обрабатывать строки "a&nbsp;&nbsp;&nbsp;&nbsp;b", "a b" и "a\nb" как одинаковые.
from sys import stdin

query = input().lower()
file_names_with_result = []

for line in stdin:
    file_name = line.rstrip('\n')
    with open(file_name, 'r', encoding='UTF-8') as file:
        content = file.read()
        content_without_space_symbol = content.replace('&nbsp;', ' ')
        formatted_content = ' '.join(content_without_space_symbol.lower().split())

        if query in formatted_content:
            file_names_with_result.append(file_name)
            continue

if not file_names_with_result:
    print('404. Not Found')
else:
    print(*file_names_with_result, sep='\n')
