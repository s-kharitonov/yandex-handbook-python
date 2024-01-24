# Отчёт неуспеваемости
# Продолжим обрабатывать DataFrame из прошлой задачи.
#
# Напишите функцию need_to_work_better, которая выбирает тех, у кого есть хотя бы одна двойка.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.


def need_to_work_better(journal):
    return journal[(journal['maths'] == 2) | (journal['physics'] == 2) | (journal['computer science'] == 2)]
