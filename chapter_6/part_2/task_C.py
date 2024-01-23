# Чек - 2
# В местном магазине решили добавить анализ данных и каждый чек представлять в виде DataFrame.
# Прайс-лист уже сформирован в виде объекта Series, где индексами являются названия, а значениями — цены.
#
# Напишите функцию, cheque, которая принимает прайс-лист и список покупок в виде
# неопределённого количества именованных параметров (ключ — название товара, значение — количество).
#
# Функция должна вернуть объект DataFrame со столбцами:
#
# наименование продукта (product);
# цена за единицу (price);
# количество (number);
# итоговая цена (cost).
# Строки чека должны быть отсортированы по названию продуктов в лексикографическом порядке.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import pandas as pd


def cheque(price_list, **kwargs):
    sorted_products = sorted(kwargs)
    total = {
        'product': sorted_products,
        'price': [price_list[product] for product in sorted_products],
        'number': [kwargs[product] for product in sorted_products],
        'cost': [price_list[product] * kwargs[product] for product in sorted_products]
    }
    return pd.DataFrame(total)
