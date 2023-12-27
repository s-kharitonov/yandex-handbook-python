# Преобразование в строку
# Вашему решению предоставлен список натуральных чисел numbers.
#
# Напишите выражение для генерации строки, представляющей собой отсортированный список чисел,
# записанных через дефис, окружённый пробелами, без повторений.
#
# Примечание
# В решении не должно быть ничего, кроме выражения.
' - '.join(str(number) for number in sorted(set(numbers)))
