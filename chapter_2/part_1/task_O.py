# В ожидании доставки
# Сегодня в N часов M минут хозяин магазина заказал доставку нового товара. 
# Оператор сказал, что продукты доставят через T минут.
# Сколько будет времени на электронных часах, когда привезут долгожданные продукты?

# Формат ввода
# В первой строке записано натуральное число 0≤N<24).
# Во второй строке записано натуральное число 0≤M<60).
# В третьей строке записано натуральное число 30≤T<10^9).

# Формат вывода
# Одна строка, представляющая циферблат электронных часов.
hours = int(input())
minutes = int(input())
delivery_time = int(input())
delivery_hours = int(delivery_time / 60)
delivery_minutes = delivery_time - delivery_hours * 60 + minutes

delivery_hours += int(delivery_minutes / 60)
delivery_hours += hours

clock_minutes = delivery_minutes % 60
clock_hours = delivery_hours % 24

print(f'{clock_hours:0>2}:{clock_minutes:0>2}')