# Украшение чека
# Давайте приведём в порядок чек, который печатали ранее.
# Все строки должны быть длиной в 35 символов.

# Формат ввода
# Название товара;
# цена товара;
# вес товара;
# количество денег у пользователя.
# Формат вывода
# Красивый чек в формате:

# ================Чек================
# Товар:                    <продукт>
# Цена:     <число>кг * <число>руб/кг
# Итого:                   <число>руб
# Внесено:                 <число>руб
# Сдача:                   <число>руб
# ===================================
name = input()
price = int(input())
weight = int(input())
money = int(input())
total = price * weight
change = money - total

price_formatted = f'{weight}кг * {price}руб/кг'
total_formatted = f'{total}руб'
money_formatted = f'{money}руб'
change_formatted = f'{change}руб'

print(f'{"Чек":=^35}')
print(f'Товар:{name: >29}')
print(f'Цена:{price_formatted: >30}')
print(f'Итого:{total_formatted: >29}')
print(f'Внесено:{money_formatted: >27}')
print(f'Сдача:{change_formatted: >29}')
print('=' * 35)