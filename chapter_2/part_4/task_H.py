# Максимальная сумма
# Ребята в детском саду снова играют с числами.
# И пусть числа они знают плохо, придумывать их они очень любят.
# Они договорились, что будут называть числа по очереди и тот,
# кто назовёт число с наибольшей суммой цифр, будет считаться победителем. \
# В качестве судьи они выбрали бедную воспитательницу, и она попросила нас о помощи.
# Напишите программу, которая определит победителя.
#
# Формат ввода
# В первой строке записано число N — количество детей в группе.
# Далее вводятся имя ребенка и его число (каждое на своей строке).
#
# Формат вывода
# Требуется вывести имя победителя.
# Если два ребенка назвали числа с одинаковой суммой цифр,
# победителем должен быть признан тот, кто ходил позже.
children_count = int(input())
winner_name = ''
winner_digits_sum = 0

for i in range(children_count):
    child_name = input()
    number = int(input())
    digits_sum = 0

    while number != 0:
        last_digit = number % 10
        number //= 10
        digits_sum += last_digit

    if digits_sum >= winner_digits_sum:
        winner_name = child_name
        winner_digits_sum = digits_sum

print(winner_name)