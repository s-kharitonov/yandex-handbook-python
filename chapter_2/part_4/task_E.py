# Зайка — 5
# В долгой дороге дети вновь заскучали, и родителям приходится их развлекать поиском зверушек за окном.
# Давайте вместе с ними найдём заек.
#
# Формат ввода
# В первой строке указано натуральное число N — количество выделенных придорожных местностей.
# В последующих строках записаны слова характеризующие выделенную местность.
# Информация о каждой местности завершается словом «ВСЁ».
#
# Формат вывода
# Количество местностей, в которых есть зайка.
descriptions_count = int(input())
descriptions_with_hares_count = 0

for i in range(descriptions_count):
    has_hares = False

    while (description_part := input()) != 'ВСЁ':
        if not has_hares and 'зайка' in description_part.lower():
            has_hares = True

    if has_hares:
        descriptions_with_hares_count += 1

print(descriptions_with_hares_count)
