# Таблица истинности 2
# Продолжим работу с таблицами истинности.
# Продумайте программу, которая для введённого сложного логического высказывания строит таблицу истинности.
#
# Формат ввода
# Вводится логическое выражение от нескольких переменных валидное для языка Python.
#
# Формат вывода
# Выведите таблицу истинности данного выражения.
from itertools import product, combinations

python_code_expression = input()
variables = sorted(set(letter for letter in python_code_expression if letter.isupper()))
all_possible_values = product(variables, [0, 1])
all_combinations = combinations(all_possible_values, len(variables))
all_combinations_with_unique_vars = filter(
    lambda vars_combination: len([variable for variable, value in vars_combination]) == len(
        {variable for variable, value in vars_combination}),
    all_combinations
)

print(*variables, 'F', sep=' ')
for combination in all_combinations_with_unique_vars:
    code_execution_result = eval(python_code_expression, {variable: value for variable, value in combination})
    values = [value for variable, value in combination]
    print(*values, 1 if code_execution_result else 0, sep=' ')
