# Кашееды — 3
# Вернёмся к условию, когда каждый воспитанник детского сада любит либо манную, либо овсяную, либо обе эти каши.
# Напишите программу, которая позволит воспитателю узнать, какие дети любят только одну кашу.
#
# Формат ввода
# В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
# Затем идут N+M строк — перемешанные фамилии детей.
# Гарантируется, что в группе нет однофамильцев.
#
# Формат вывода
# В алфавитном порядке фамилии учеников, которые любят только одну кашу.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».
semolina_lovers_count = int(input())
oatmeal_lovers_count = int(input())
porridge_lovers = {}

for i in range(semolina_lovers_count + oatmeal_lovers_count):
    child = input()
    favorite_porridge_count = porridge_lovers.get(child, 0)

    porridge_lovers[child] = favorite_porridge_count + 1

children_with_one_favorite_porridge = []

for child in porridge_lovers:
    favorite_porridge_count = porridge_lovers[child]

    if favorite_porridge_count == 1:
        children_with_one_favorite_porridge.append(child)

if len(children_with_one_favorite_porridge) > 0:
    children_with_one_favorite_porridge.sort()
    print('\n'.join(children_with_one_favorite_porridge))
else:
    print('Таких нет')
