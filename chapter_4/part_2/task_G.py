# В эфире рубрика «Эксперименты»
# Лаборанты проводят эксперимент и запросили разработку системы обработки данных.
# Результатами эксперимента должны стать пары рациональных чисел.
#
# Для работы им требуются функции:
#
# enter_results(first, second, ...) — добавление данных одного или нескольких результатов
# (гарантируется, что количество параметров будет чётным);
# get_sum() — возвращает пару сумм результатов экспериментов;
# get_average() — возвращает пару средних арифметических значений результатов экспериментов.
# Все вычисления производятся с точностью до сотых.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.
even_index_numbers = []
odd_index_numbers = []


def enter_results(*numbers):
    for i, number in enumerate(numbers):
        if i % 2 == 0:
            even_index_numbers.append(number)
        else:
            odd_index_numbers.append(number)


def get_sum():
    sums = (sum(even_index_numbers), sum(odd_index_numbers))
    return sums


def get_average():
    sums = get_sum()
    even_index_avg = round(sums[0] / len(even_index_numbers), 2)
    odd_index_avg = round(sums[1] / len(odd_index_numbers), 2)
    averages = (even_index_avg, odd_index_avg)
    return averages
