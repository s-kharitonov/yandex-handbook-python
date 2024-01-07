# Таблицы истинности 3
# Продолжим работу с таблицами истинности.
# К сожалению, некоторые из операций Булевой алгебры не реализованы в Python.
# Самые частые не стандартные операции это: импликация, строгая дизъюнкция и эквивалентность.
#
# Обозначим их следующим образом:
#
# импликация — ->;
# строгая дизъюнкция — ^;
# эквивалентность — ~.
# Напишите программу, которая для введённого сложного логического высказывания строит таблицу истинности.
#
# Формат ввода
# Вводится логическое выражение от нескольких переменных.
#
# Возможное содержание выражения:
#
# Заглавная латинская буква — переменная;
# not — отрицание;
# and — конъюнкция;
# or — дизъюнкция;
# ^ — строгая дизъюнкция;
# -> — импликация;
# ~ — эквивалентность;
# () — логические скобки.
# Формат вывода
# Выведите таблицу истинности данного выражения.
#
# Примечание
# Прежде, чем реализовывать новые операции, обратите внимание на их приоритет.
# Рекомендуем воспользоваться знаниями полученными при решении задачи «Польский калькулятор».
from itertools import combinations, product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

OPERATORS_PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def parse_expression(expression, variables):
    expression_parts_stack = []
    parsed_expression_parts = []
    expression_parts = expression.replace('(', '( ').replace(')', ' )').split()

    for part in expression_parts:
        if part in variables:
            parsed_expression_parts.append(part)
            continue
        if part == '(':
            expression_parts_stack.append(part)
            continue
        if part == ')':
            while expression_parts_stack[-1] != '(':
                parsed_expression_parts.append(OPERATORS[expression_parts_stack.pop()])
            expression_parts_stack.pop()
            continue
        if part in OPERATORS.keys():
            priority = OPERATORS_PRIORITY[part]

            while len(expression_parts_stack) and priority >= OPERATORS_PRIORITY[expression_parts_stack[-1]]:
                parsed_expression_parts.append(OPERATORS[expression_parts_stack.pop()])
            expression_parts_stack.append(part)
            continue
    for i in range(len(expression_parts_stack)):
        parsed_expression_parts.append(OPERATORS[expression_parts_stack.pop()])

    return parsed_expression_parts


def eval_expression(expression_parts, variables):
    expression_parts_stack = []

    for i, part in enumerate(expression_parts):
        if part in variables.keys():
            expression_parts_stack.append(variables[part])
            continue
        if part == 'not':
            expression_parts_stack.append(not expression_parts_stack.pop())
            continue

        second_part = expression_parts_stack.pop()
        first_part = expression_parts_stack.pop()
        expression_parts_stack.append(eval(f'{first_part} {part} {second_part}'))

    return int(expression_parts_stack.pop())


expression = input()
variables = sorted(set(letter for letter in expression if letter.isupper()))
all_possible_values = product(variables, [0, 1])
all_combinations = combinations(all_possible_values, len(variables))
all_combinations_with_unique_vars = filter(
    lambda vars_combination: len([variable for variable, value in vars_combination]) == len(
        {variable for variable, value in vars_combination}),
    all_combinations
)
parsed_expression = parse_expression(expression, variables)

print(*variables, 'F', sep=' ')
for combination in all_combinations_with_unique_vars:
    code_execution_result = eval_expression(parsed_expression, {variable: value for variable, value in combination})
    values = [value for variable, value in combination]
    print(*values, 1 if code_execution_result else 0, sep=' ')
