# Средний рост
# Учитель физкультуры задался вопросом, на сколько в среднем его подопечные выросли за прошедший месяц.
#
# Напишите программу, которая определяет, на сколько изменился средний рост учеников в классе.
#
# Формат ввода
# Вводится информация о детях в формате:
# <Имя> <Рост месяц назад> <Рост сейчас>
#
# Формат вывода
# Одно число — ответ на вопрос задачи.
# Ответ округлите до целых. Например, функцией round.
from sys import stdin

heights = []

for line in stdin:
    name, prev_height, current_height = line.split()
    heights.append(int(current_height) - int(prev_height))

avg = round(sum(heights) / len(heights), 0)

print(f'{avg:.0f}')