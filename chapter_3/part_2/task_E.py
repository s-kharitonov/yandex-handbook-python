# Кашееды — 2
# Изменим задачу и напишем программу, которая поможет быстро выяснить, сколько детей любят только одну кашу.
#
# Формат ввода
# В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
# Затем идут N+M строк — перемешанные фамилии детей.
# Гарантируется, что в группе нет однофамильцев.
#
# Формат вывода
# Количество учеников, которые любят только одну кашу.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».
semolina_lovers_count = int(input())
oatmeal_lovers_count = int(input())
unique_porridge_lovers = set()
duplicates_count = 0

for i in range(semolina_lovers_count + oatmeal_lovers_count):
    child = input()

    if child in unique_porridge_lovers:
        duplicates_count += 1
    else:
        unique_porridge_lovers.add(child)

unique_porridge_lovers_count = len(unique_porridge_lovers) - duplicates_count

if unique_porridge_lovers_count > 0:
    print(unique_porridge_lovers_count)
else:
    print('Таких нет')
