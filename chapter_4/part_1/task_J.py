# Слияние
# Напишите функцию merge, которая принимает два отсортированных по возрастанию кортежа целых чисел,
# а возвращает один из всех переданных чисел.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
# В этой задаче отключены стандартные сортировки

def merge(first_numbers, second_numbers):
    result = []
    first_pointer = 0
    second_pointer = 0

    while first_pointer < len(first_numbers) and second_pointer < len(second_numbers):
        first_number = first_numbers[first_pointer]
        second_number = second_numbers[second_pointer]

        if first_number <= second_number:
            first_pointer += 1
            result.append(first_number)
        else:
            second_pointer += 1
            result.append(second_number)

    while first_pointer < len(first_numbers):
        result.append(first_numbers[first_pointer])
        first_pointer += 1

    while second_pointer < len(second_numbers):
        result.append(second_numbers[second_pointer])
        second_pointer += 1

    return tuple(result)
