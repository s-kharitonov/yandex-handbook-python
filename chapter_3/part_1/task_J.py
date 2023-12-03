# Частотный анализ на минималках
# Частотный анализ — подсчёт, какие символы чаще всего встречаются в тексте.
# Это важнейший инструмент взлома многих классических шифров — от шифра Цезаря и до шифровальной машины «Энигма». \
# Выполним простой частотный анализ: выясним, какой символ встречается в тексте чаще всего.
#
# Формат ввода
# Вводятся строки, пока не будет введена строка «ФИНИШ».
#
# Формат вывода
# Выводится один символ в нижнем регистре — наиболее часто встречающийся.
letters = []
counters = []
best_letter = None
best_letter_counter = 0

while (phrase := input()) != 'ФИНИШ':
    for letter in phrase:
        if letter == ' ':
            continue

        lower_letter = letter.lower()

        try:
            letter_position = letters.index(lower_letter)
        except ValueError:
            letters.append(lower_letter)
            counters.append(0)
            letter_position = len(letters) - 1

        counter = counters[letter_position]
        counter += 1
        counters[letter_position] = counter

        if counter > best_letter_counter or (counter == best_letter_counter and lower_letter < best_letter):
            best_letter_counter = counter
            best_letter = lower_letter

print(best_letter)
