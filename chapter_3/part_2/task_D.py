# Кашееды
# Каждый воспитанник детского сада любит либо манную, либо овсяную, либо обе каши.
# Давайте создадим программу, которая позволит воспитателю быстро выяснить, сколько детей любят обе каши.
#
# Формат ввода
# В первых двух строках указывается количество детей, любящих манную и овсяную каши (N и M).
# Затем идут N строк — фамилии детей, которые любят манную кашу, и M строк с фамилиями детей, любящих овсяную кашу.
# Гарантируется, что в группе нет однофамильцев.
#
# Формат вывода
# Количество учеников, которые любят обе каши.
# Если таких не окажется, в строке вывода нужно написать «Таких нет».
semolina_lovers_count = int(input())
oatmeal_lovers_count = int(input())
semolina_lovers = set()
oatmeal_lovers = set()

for i in range(semolina_lovers_count):
    child = input()
    semolina_lovers.add(child)

for i in range(oatmeal_lovers_count):
    child = input()
    oatmeal_lovers.add(child)

porridge_lovers = semolina_lovers & oatmeal_lovers
porridge_lovers_count = len(porridge_lovers)

if porridge_lovers_count > 0:
    print(porridge_lovers_count)
else:
    print('Таких нет')
