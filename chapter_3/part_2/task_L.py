# Однофамильцы — 2
# Вновь поможем сотруднику из отдела кадров выяснить,
# сколько мужчин-однофамильцев работает в организации, но уже немного с иными условиями.
#
# Формат ввода
# В первой строке указывается количество мужчин — сотрудников организации (N).
# Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.
#
# Формат вывода
# Список однофамильцев в организации с указанием их количества в алфавитном порядке.
# Если таковых нет — вывести «Однофамильцев нет».
mens_count = int(input())
mens_count_by_name = dict()

for i in range(mens_count):
    men = input()
    counter = mens_count_by_name.get(men, 0)

    counter += 1
    mens_count_by_name[men] = counter

mens = []

for mens_name_with_counter in mens_count_by_name.items():
    counter = mens_name_with_counter[1]

    if counter > 1:
        mens.append(mens_name_with_counter)

if mens:
    mens.sort()
    for men, counter in mens:
        if counter > 1:
            print(f'{men} - {counter}')
else:
    print('Однофамильцев нет')
