# Легенды велогонок возвращаются: кто быстрее?
# В новом сезоне за первенство в велогонках вновь борются лучшие из лучших. 
# Протяжённость заключительной трассы — 43872м, и все хотят знать, кто получит золотую медаль.

# Нам известны средние скорости трёх претендентов на победу – Пети, Васи и Толи. Кто из них победит?

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Красивый пьедестал (ширина ступеней 8 символов).
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

if tolya_speed <= vasya_speed <= petya_speed:
    print(f'{"Петя": ^24}')
    print(f'{"  Вася": <20}')
    print(f'{"Толя": >22}')
    print('   II      I      III   ')
elif vasya_speed <= tolya_speed <= petya_speed:
    print(f'{"Петя": ^24}')
    print(f'{"  Толя": <20}')
    print(f'{"Вася": >22}')
    print('   II      I      III   ')
elif petya_speed <= tolya_speed <= vasya_speed:
    print(f'{"Вася": ^24}')
    print(f'{"  Толя": <20}')
    print(f'{"Петя": >22}')
    print('   II      I      III   ')
elif petya_speed <= vasya_speed <= tolya_speed:
    print(f'{"Толя": ^24}')
    print(f'{"  Вася": <20}')
    print(f'{"Петя": >22}')
    print('   II      I      III   ')
elif vasya_speed <= petya_speed <= tolya_speed:
    print(f'{"Толя": ^24}')
    print(f'{"  Петя": <20}')
    print(f'{"Вася": >22}')
    print('   II      I      III   ')
else:
    print(f'{"Вася": ^24}')
    print(f'{"  Петя": <20}')
    print(f'{"Толя": >22}')
    print('   II      I      III   ')