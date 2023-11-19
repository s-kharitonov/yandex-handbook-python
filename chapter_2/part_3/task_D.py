# Считалочка 2.0
# Дети продолжают запоминать цифры, а мы им помогать.
# Нам вновь называют начало и конец последовательности чисел, а мы выводим их и числа между.
#
# Формат ввода
# Два числа, каждое с новой строки.
#
# Формат вывода
# Все числа от начала до конца (включительно), записанные через пробел.
from_number = int(input())
to_number = int(input())
step = 1
result = ''

if to_number < from_number:
    step = -1
    to_number -= 1
else:
    to_number += 1

for i in range(from_number, to_number, step):
    result += str(i) + ' '
print(result, end='')
