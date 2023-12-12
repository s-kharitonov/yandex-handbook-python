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
porridge_lovers = {}
duplicates_count = 0

for i in range(semolina_lovers_count + oatmeal_lovers_count):
    child = input()
    favorite_porridge_count = porridge_lovers.get(child, 0)

    porridge_lovers[child] = favorite_porridge_count + 1

children_count_with_1_favorite_porridge = 0

for child in porridge_lovers:
    favorite_porridge_count = porridge_lovers[child]

    if favorite_porridge_count == 1:
        children_count_with_1_favorite_porridge += 1

if children_count_with_1_favorite_porridge > 0:
    print(children_count_with_1_favorite_porridge)
else:
    print('Таких нет')
