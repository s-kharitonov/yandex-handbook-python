# Территория зла
# В давние времена считалось, что если какая-то местность является треугольником, 
# то в ней заключено страшное зло.

# При этом люди оценивали риск встретить зло по форме этого треугольника:

# в остроугольном треугольнике вероятность встретить зло крайне мала;
# в тупоугольном — велика;
# в прямоугольном — 100%.
# Напишите программу, которая по длине сторон треугольной местности, 
# определяет вероятность встретить зло.

# Формат ввода
# Три числа — длины сторон треугольной местности.

# Формат вывода
# Вероятность встретить зло согласно поверью:

# крайне мала;
# велика;
# 100%.
first_length = int(input())
second_length = int(input())
third_length = int(input())
max_length = max(first_length, second_length, third_length)
min_length = min(first_length, second_length, third_length)
mid_length = first_length + second_length + third_length - max_length - min_length
max_length_squared = max_length ** 2
min_length_squared = min_length ** 2
mid_length_squared = mid_length ** 2
sum = min_length_squared + mid_length_squared

if max_length_squared > sum:
    print('велика')
elif max_length_squared == sum:
    print('100%')
else:
    print('крайне мала')