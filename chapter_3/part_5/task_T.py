# Файловая сумма
# Вы скорее всего знаете, что существуют не только текстовые файлы.
# Различные форматы данных предусматривают специальное кодирование.
# Например, BMP изображения хранят некоторую заголовочную информацию и цвета всех пикселей в виде чисел.
#
# Давайте поработаем с такими данными.
# Нам дают файл в некотором формате, назовем его NUM.
# Он содержит список 2-байтных чисел.
# Для простоты будем считать, что отрицательных чисел не существует.
#
# Напишите программу, которая вычисляет сумму всех записанных в файле чисел в 2-байтном диапазоне.
#
# Формат ввода
# В файле numbers.num содержатся числа в указанном формате.
#
# Формат вывода
# Одно число — сумма всех чисел в файле на 2-байтном диапазоне.

with open('numbers.num', 'rb') as numbers_file:
    content = numbers_file.read()
    numbers = [int.from_bytes(content[i:i + 2], 'big') for i in range(0, len(content), 2)]
    print(sum(numbers) % 2**16)