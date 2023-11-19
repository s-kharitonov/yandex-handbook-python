# Считалочка
# Ребята в детском саду учат числа, и мы можем им в этом помочь.
# Ребята дают нам два числа — начало и конец последовательности чисел.
# Наша задача вывести все числа от начала до конца, заполнив промежуток между ними.
#
# Формат ввода
# Два числа в порядке возрастания, каждое с новой строки.
#
# Формат вывода
# Все числа от начала до конца (включительно), записанные через пробел.
from_number = int(input())
to_number = int(input())
result = ''

for i in range(from_number, to_number + 1):
    result += str(i) + ' '
print(result, end='')
