# Таблица истинности
# Вся современная электронно-вычислительная техника строится на Булевой алгебре,
# которая оперирует истинностью и ложностью высказываний.
# Любой язык программирования содержит логические операции (в Python это and, or, not).
#
# Чаще всего для работы со сложными высказываниями прибегают к методу под названием «Таблица истинности».
# Суть метода проста — рассматриваются все возможные значения входных переменных и для них вычисляется результат.
#
# Разработайте программу, которая для введённого сложного логического высказывания строит таблицу истинности.
#
# Формат ввода
# Вводится логическое выражение от трех переменных (a, b, c) валидное для языка Python.
#
# Формат вывода
# Выведите таблицу истинности данного выражения.
from itertools import product, combinations

python_code_expression = input()
all_possible_values = product(['a', 'b', 'c'], [0, 1])
all_combinations = combinations(all_possible_values, 3)
all_combinations_with_unique_vars = filter(lambda x: x[0][0] != x[1][0] != x[2][0], all_combinations)

print('a b c f')
for a, b, c in all_combinations_with_unique_vars:
    code_execution_result = eval(python_code_expression, {"a": a[1], "b": b[1], "c": c[1]})
    print(f'{a[1]} {b[1]} {c[1]} {1 if code_execution_result else 0}')
