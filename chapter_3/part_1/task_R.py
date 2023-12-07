# RLE
# RLE означает “run-length encoding”.
# Это способ сокращённой записи последовательности чего угодно (в случае этой задачи — цифр).
# При нём для подряд идущей группы одинаковых цифр (run) записываются сама эта цифра и длина этой группы (run length).
# Таким образом, 99999 превратится в 9 5 («девять пять раз») и так далее.
# RLE широко используется в самых разных областях.
# Напишите программу, которая кодирует строку цифр в RLE.
#
# Формат ввода
# Строка цифр длиной не меньше 1.
#
# Формат вывода
# Пары: сама цифра и количество повторений цифры подряд во введённой строке, как описано в условии и показано в примере.
digits = input()
prev_digit = digits[0]
digit_counter = 1

if len(digits) == 1:
    print(f'{prev_digit} 1')

for i in range(1, len(digits)):
    digit = digits[i]
    if digit == prev_digit:
        digit_counter += 1
    else:
        print(f'{prev_digit} {digit_counter}')
        prev_digit = digit
        digit_counter = 1
else:
    print(f'{prev_digit} {digit_counter}')
