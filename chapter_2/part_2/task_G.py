# А роза упала на лапу Азора
# Существуют такое интересное понятие как палиндром — число, слово, 
# предложение и так далее, которое и слева-направо, и справа-налево читается одинаково.

# Напишите программу, которая проверяет, является ли число палиндромом.

# Формат ввода
# Одно четырёхзначное число

# Формат вывода
# YES если число является палиндромом, иначе — NO.
number = int(input())
first_number = str(number // 1000)
second_number = str(number // 100 % 10)
third_number = str(number // 10 % 10)
fourth_number = str(number % 10)
palindrome = fourth_number + third_number + second_number + first_number

if number == int(palindrome):
    print('YES')
else:
    print('NO')