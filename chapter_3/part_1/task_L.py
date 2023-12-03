# Меню питания
# В детском саду ежедневно подают новую кашу на завтрак.
# Каши чередуются в следующем порядке:
#
# Манная;
# Гречневая;
# Пшённая;
# Овсяная;
# Рисовая.
# Напишите программу, которая строит расписание каш на ближайшие дни.
#
# Формат ввода
# Вводится натуральное число N — количество дней.
#
# Формат вывода
# Вывести список каш в порядке подачи.
schedule = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
days_count = int(input())
schedule_length = len(schedule)
schedule_by_days = None

if days_count <= schedule_length:
    schedule_by_days = schedule[:days_count]
else:
    remainder = days_count % schedule_length
    multiplier = days_count // schedule_length
    schedule_by_days = schedule * multiplier + schedule[:remainder]

result = '\n'.join(schedule_by_days)
print(result)
