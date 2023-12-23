# Однофамильцы
# Начальник кадровой службы хочет выяснить, сколько мужчин-однофамильцев работает в организации.
# У него есть список фамилий, и на основании этого списка нужно вычислить количество фамилий,
# которые совпадают с другими.
#
# Формат ввода
# В первой строке указывается количество мужчин — сотрудников организации (N).
# Затем идут N строк с фамилиями этих сотрудников в произвольном порядке.
#
# Формат вывода
# Количество однофамильцев в организации.
mens_count = int(input())
mens_count_by_name = dict()

for i in range(mens_count):
    men = input()
    counter = mens_count_by_name.get(men, 0)

    counter += 1
    mens_count_by_name[men] = counter

namesakes_count = 0

for men in mens_count_by_name:
    counter = mens_count_by_name[men]

    if counter > 1:
        namesakes_count += counter

print(namesakes_count)
