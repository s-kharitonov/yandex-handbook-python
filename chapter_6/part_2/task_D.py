# Акция
# Магазин, для которого вы писали функцию в предыдущей задаче, проводит акцию:
#
# При покупке больше двух товаров — скидка 50%
#
# мелкий шрифт: скидка распространяется только на товары купленные в количестве более двух штук
#
# Напишите функцию discount, принимающую чек из прошлой задачи и возвращающую новый с учётом акции.
#
# Примечание
# Не удаляйте функцию cheque, она потребуется для тестирования.
#
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


def discount(cheque):
    costs = [(cost - cost * 0.5) if cheque.loc[i, 'number'] > 2 else cost for i, cost in enumerate(cheque['cost'])]

    return pd.DataFrame({
        'product': cheque['product'],
        'price': cheque['price'],
        'number': cheque['number'],
        'cost': costs
    })
