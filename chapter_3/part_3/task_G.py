# Делители
# Вашему решению будет предоставлено множество numbers.
#
# Продумайте выражение для генерации словаря содержащего информацию о делителях каждого из заданных чисел.
#
# Примечание
# В решении не должно быть ничего, кроме выражения.
{number: [i for i in range(1, number + 1) if number % i == 0] for number in numbers}
