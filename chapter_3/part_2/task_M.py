# Дайте чего-нибудь новенького!
# Главный повар детского сада хочет приготовить в праздничный день блюда, которые ни разу не готовил на этой неделе.
# В его распоряжении есть список блюд:
# - которые можно приготовить в столовой сегодня;
# - которые были приготовлены в каждый из дней недели.

# Формат ввода
# Число блюд (N), которые можно приготовить в столовой.
# N строк с названиями блюд. Число дней (M), о которых имеется информация.
# M блоков строк для каждого из списков.
# В первой строке каждого блока записано число блюд в заданный день, затем перечисляются эти блюда.
#
# Формат вывода
# Список блюд, которые ещё не готовились на этой неделе в алфавитном порядке.
# Если все возможные блюда уже были приготовлены, следует вывести «Готовить нечего».
dishes_count = int(input())
available_dishes_today = set()
cooked_dishes_this_week = set()

for i in range(dishes_count):
    dish = input()
    available_dishes_today.add(dish)

days_count = int(input())

for i in range(days_count):
    day_dishes_count = int(input())

    for j in range(day_dishes_count):
        dish = input()
        cooked_dishes_this_week.add(dish)

dishes_difference = []

for dish in available_dishes_today:
    if dish in cooked_dishes_this_week:
        continue

    dishes_difference.append(dish)

if dishes_difference:
    dishes_difference.sort()
    print('\n'.join(dishes_difference))
else:
    print('Готовить нечего')
