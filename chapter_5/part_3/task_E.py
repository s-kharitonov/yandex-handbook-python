# Слияние с проверкой
# Когда-то вы уже писали функцию merge, которая производит слияние двух отсортированных кортежей.
#
# Давай-те её немного переработаем.
#
# Введём систему проверок:
#
# если один из параметров не является итерируемым объектом, то вызовите исключение StopIteration;
# если значения входных параметров содержат «неоднородные» данные, то вызовите исключение TypeError;
# если один из параметров не отсортирован, то вызовите исключение ValueError.
# Проверки следует проводить в указанном порядке.
#
# Если параметры прошли все проверки, верните итерируемый объект, являющийся слиянием двух переданных.
#
# Примечание
# В решении не должно быть вызовов требуемых функций.


def merge(iterable1, iterable2):
    try:
        iterator1 = iter(iterable1)
        iterator2 = iter(iterable2)
    except TypeError:
        raise StopIteration
    if any(not isinstance(element, type(iterable1[0])) for element in iterable1):
        raise TypeError
    if any(not isinstance(element, type(iterable1[0])) for element in iterable2):
        raise TypeError
    if list(iterable1) != sorted(iterable1) or list(iterable2) != sorted(iterable2):
        raise ValueError
    return tuple(sorted(list(iterable1) + list(iterable2)))
