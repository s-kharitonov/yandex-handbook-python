# Обновление журнала
# Продолжим обрабатывать DataFrame из прошлых задач.
#
# Напишите функцию update, которая добавляет к данным столбец average, содержащий среднюю оценку ученика,
# а также сортирует данные по убыванию этого столбца, а при равенстве средних — по имени лексикографически.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.


def update(journal):
    journal_copy = journal.copy()
    journal_copy['average'] = journal_copy[['maths', 'physics', 'computer science']].mean(axis=1)
    return journal_copy.sort_values(by=['average', 'name'], ascending=(False, True))
