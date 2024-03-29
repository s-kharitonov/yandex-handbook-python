# Бесконечный морской бой
# Представьте себе поле морского боя, которое не имеет границ.
# Для простоты координаты выстрелов будем обозначать целыми координатами на плоскости.
#
# Бесконечное поле порождает большое количество данных, которые требуется проанализировать.
# Один из игроков для упрощения этой задачи просит вас написать программу,
# которая обрезает данные до ограниченного прямоугольника.
#
# Формат ввода
# В первой строке записано два числа — координаты верхнего левого угла. Во второй строке — правого нижнего.
#
# В файле data.csv находится датасет с координатами всех выстрелов противника.
#
# Формат вывода
# Часть датасета, ограниченная заданным прямоугольником.
import pandas as pd

a, b = map(int, input().split())
c, d = map(int, input().split())
field = pd.read_csv('data.csv')

print(field[(a <= field['x']) & (field['x'] <= c) & (d <= field['y']) & (field['y'] <= b)])
