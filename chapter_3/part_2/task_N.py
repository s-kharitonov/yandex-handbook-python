# Это будет шедевр!
# Главный повар детского сада хочет быстрее выбирать блюда для готовки.
# В его распоряжении есть список продуктов, а также набор блюд.
#
# Напишите программу, способную быстро определить блюда, которые можно приготовить.
#
# Формат ввода
# Число продуктов (N), которые имеются в наличии. N строк с названиями продуктов.
# Число рецептов (M), о которых имеется информация. M блоков строк для каждого из рецептов.
# В первой строке каждого блока записано название блюда.
# Во второй — число ингредиентов.
# Затем перечисляются сами ингредиенты, требуемые для приготовления блюда.
#
# Формат вывода
# Список блюд, которые можно приготовить в алфавитном порядке.
# Если ни одно из блюд нельзя приготовить, следует вывести «Готовить нечего».
available_products_count = int(input())
available_products = set()
available_dishes = []

for i in range(available_products_count):
    product_name = input()
    available_products.add(product_name)

recipes_count = int(input())

for i in range(recipes_count):
    dish = input()
    ingredients_count = int(input())
    ingredients = set()

    for j in range(ingredients_count):
        ingredient = input()
        ingredients.add(ingredient)

    if ingredients <= available_products:
        available_dishes.append(dish)

if available_dishes:
    available_dishes.sort()
    print('\n'.join(available_dishes))
else:
    print('Готовить нечего')

