# Польский калькулятор — 2
# Потренируемся в ОПН дальше. Операции, которые выполняются с одним значением, называются унарными,
# с двумя — бинарными, с тремя — тернарными. Давайте улучшим наш калькулятор, добавив поддержку следующих операций:
#
# бинарные:
# + (сложение),
# - (вычитание),
# * (умножение),
# / (деление нацело; для отрицательных чисел работает по тем же правилам, что и в Python);
# унарные:
# ~ (унарный минус — меняет знак),
# ! (факториал),
# # (клонирование — вернуть в стек значение дважды);
# тернарные:
# @ (возвращает в стек те же три значения, но в ином порядке: второе, третье, первое).
# Формат ввода
# Вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций.
# Вместе они составляют корректное выражение в обратной польской нотации,
# не содержащее деления на ноль и взятия факториала от отрицательного числа.
#
# Формат вывода
# Выводится одно целое число — результат вычисления выражения.
numbers_with_operations = input().split()
stack = []

for element in numbers_with_operations:
    if element.isdecimal():
        stack.append(int(element))
        continue

    match element:
        case '+':
            first_number = stack.pop()
            second_number = stack.pop()

            stack.append(second_number + first_number)
        case '-':
            first_number = stack.pop()
            second_number = stack.pop()

            stack.append(second_number - first_number)
        case '*':
            first_number = stack.pop()
            second_number = stack.pop()

            stack.append(second_number * first_number)
        case '/':
            first_number = stack.pop()
            second_number = stack.pop()

            stack.append(second_number // first_number)
        case '~':
            number = stack.pop()

            stack.append(-number)
        case '!':
            number = stack.pop()
            factorial = 1

            for i in range(1, number + 1):
                factorial *= i

            stack.append(factorial)
        case '#':
            number = stack.pop()

            stack.append(number)
            stack.append(number)
        case '@':
            first_number = stack.pop()
            second_number = stack.pop()
            third_number = stack.pop()

            stack.append(second_number)
            stack.append(first_number)
            stack.append(third_number)

print(stack[0])
