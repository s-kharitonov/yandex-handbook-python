# Зайка — 6
# Очередное путешествие родителей с детьми, очередная игра с поиском зверушек за окном.
# Давайте поиграем и найдём заек.
#
# Формат ввода
# В первой строке записано натуральное число N — количество выделенных придорожных местностей.
# В каждой из N последующих строк записано описание придорожной местности.
#
# Формат вывода
# Количество заек.
terrain_descriptions_count = int(input())
hares_counter = 0

for i in range(terrain_descriptions_count):
    terrain_description = input()
    hares_counter += terrain_description.count('зайка')

print(hares_counter)
