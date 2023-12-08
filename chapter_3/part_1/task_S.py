# Польский калькулятор
# Напишите программу, которая производит вычисление выражения, записанного в обратной польской нотации (ОПН).
#
# В ОПН нет ни скобок, ни приоритета операторов («умножение раньше сложения»).
#
# Чтобы прочитать выражение, записанное в таком формате, нужно просматривать выражение строго последовательно.
# Вводимые значения последовательно добавляются в стек.
# Когда встречается символ операции, то из стека извлекаются последние положенные туда значения,
# с ними проделывается эта операция и результат возвращается в стек.
#
# Если для операции важен порядок значений, с которыми она производится, то первым идёт число, лежавшее в стеке глубже.
# В частности, если операция — вычитание, то из предпоследнего числа в стеке вычитается последнее, а не наоборот.
#
# Изначально стек пустой, в результате полного вычисления выражения
# в нём должно остаться одно значение — результат вычислений.
#
# Первый пример следует читать так: в стек последовательно добавляются значения 7 2 3,
# а затем встречаем знак операции *.
# Тогда значения 2 и 3 извлекаются, перемножаются, результат 6 кладётся обратно в стек.
# Следующий знак извлекает из стека два оставшихся в нём значения 7 и 6, вычитает одно
# из другого и кладёт результат снова в стек.
# Выражение закончилось, в стеке одно число — 1, это и есть результат вычисления.
#
# Формат ввода
# Вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций +, -, *,
# которые вместе составляют корректное выражение в обратной польской нотации.
#
# Формат вывода
# Выводится одно целое число — результат вычисления выражения.
numbers_with_operations = input().split()
stack = []

for element in numbers_with_operations:
    if element.isdecimal():
        stack.append(int(element))
        continue

    first_number = stack.pop()
    second_number = stack.pop()

    match element:
        case '+':
            stack.append(first_number + second_number)
        case '-':
            stack.append(second_number - first_number)
        case '*':
            stack.append(first_number * second_number)

print(stack[0])
