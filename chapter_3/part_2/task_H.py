# Кашееды — 4
# Каждый воспитанник детского сада любит одну или несколько каш.
# Поможем воспитателю составить список детей, которые любят конкретную кашу.
#
# Формат ввода
# В первой строке задаётся количество детей в группе (N).
# В следующих N строках записана фамилия ребенка и список его любимых каш.
# В последней строке записана каша, информацию о которой хочет получить воспитатель.
#
# Формат вывода
# Фамилии учеников, которые любят заданную кашу, в алфавитном порядке.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».
children_count = int(input())
children_by_porridge = dict()

for i in range(children_count):
    child_with_favorite_porridge = input().split()
    child_name = child_with_favorite_porridge[0]

    for j in range(1, len(child_with_favorite_porridge)):
        porridge = child_with_favorite_porridge[j]
        children = children_by_porridge.get(porridge, [])

        children.append(child_name)
        children_by_porridge[porridge] = children

search_porridge = input()
children = children_by_porridge.get(search_porridge, [])

if children:
    children.sort()
    print('\n'.join(children))
else:
    print('Таких нет')

