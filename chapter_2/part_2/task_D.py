# Список победителей
# Длина трассы — 43872м, и зрители хотят узнать имя победителя.

# Нам известны средние скорости трёх фаворитов – Пети, Васи и Толи. 
# Помогите подвести итоги гонки.

# Формат ввода
# В первой строке записана средняя скорость Пети.
# Во второй — Васи.
# В третьей — Толи.

# Формат вывода
# Имена победителей в порядке занятых мест.
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

if tolya_speed < vasya_speed < petya_speed:
    print('1. Петя')
    print('2. Вася')
    print('3. Толя')
elif vasya_speed < tolya_speed < petya_speed:
    print('1. Петя')
    print('2. Толя')
    print('3. Вася')
elif tolya_speed < petya_speed < vasya_speed:
    print('1. Вася')
    print('2. Петя')
    print('3. Толя')
elif petya_speed < tolya_speed < vasya_speed:
    print('1. Вася')
    print('2. Толя')
    print('3. Петя')    
elif petya_speed < vasya_speed < tolya_speed:
    print('1. Толя')
    print('2. Вася')
    print('3. Петя')
else:
    print('1. Толя')
    print('2. Петя')
    print('3. Вася') 