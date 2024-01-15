# Сортировка слиянием
# Мы уже реализовывали функцию merge, которая способна "слить" два отсортированных списка в один.
# Чаще всего её применяют в рекурсивном алгоритме сортировки слиянием.
#
# Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.
# Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показана для примера.


def merge_sort(collection):
    if len(collection) == 1:
        return collection
    left_half = merge_sort(collection[:len(collection) // 2])
    right_half = merge_sort(collection[len(collection) // 2:])
    return merge(left_half, right_half)


def merge(first_collection, second_collection):
    merged_collection = []
    first_pointer = 0
    second_pointer = 0

    while first_pointer < len(first_collection) and second_pointer < len(second_collection):
        first_element = first_collection[first_pointer]
        second_element = second_collection[second_pointer]

        if first_element <= second_element:
            first_pointer += 1
            merged_collection.append(first_element)
        else:
            second_pointer += 1
            merged_collection.append(second_element)

    while first_pointer < len(first_collection):
        first_element = first_collection[first_pointer]

        merged_collection.append(first_element)
        first_pointer += 1

    while second_pointer < len(second_collection):
        second_element = second_collection[second_pointer]

        merged_collection.append(second_element)
        second_pointer += 1

    return merged_collection
