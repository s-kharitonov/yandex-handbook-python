# Зайка — 2
# По пути домой родители вновь решили сыграть с детьми в поиск зверушек.

# Формат ввода
# Три строки описывающих придорожную местность.

# Формат вывода
# Строка в которой есть зайка, а затем её длина.
# Если таких строк несколько, выбрать ту, что меньше всех лексикографически.
first_line = input()
second_line = input()
third_line = input()
max_line = max(first_line, second_line, third_line)
min_line = min(first_line, second_line, third_line)
mid_line = first_line

if first_line != max_line and first_line != min_line:
    mid_line = first_line
elif second_line != max_line and second_line != min_line:
    mid_line = second_line
else:
    mid_line = third_line
    
if 'зайка' in min_line.lower():
    print(f'{min_line} {len(min_line)}')
elif 'зайка' in mid_line.lower():
    print(f'{mid_line} {len(mid_line)}')
else:
    print(f'{max_line} {len(max_line)}')
    