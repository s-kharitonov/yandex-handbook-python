# Расклад таков...
# Виталий любит играть в карты.
# Он решил выяснить, какие есть вариации вытащить из колоды определённые тройки карт.
# Напишите программу, которая выводит список вариантов согласно требованиям.
#
# Формат ввода
# В первой строке записана масть, которая должна присутствовать в тройке.
# Во второй строке записан достоинство, которого не должно быть в тройке.
#
# Формат вывода
# Выведите на экран первые 10 получившихся троек.
# Карты в каждой комбинации должны быть отсортированы лексикографически (по строке названия карты).
# Карты комбинации выводятся через запятую с пробелом после неё.
# Комбинации между собой также должны быть отсортированы в лексикографическом порядке по строке,
# представляющей комбинацию целиком.
from itertools import product, combinations

suit_cases = {
    'буби': 'бубен',
    'пики': 'пик',
    'трефы': 'треф',
    'черви': 'червей',
}
required_suit = input()
nominal_for_remove = input()
suits = ['буби', 'пики', 'трефы', 'черви']
nominals = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

nominals.remove(nominal_for_remove)

card_deck = product(nominals, suits)
triples_combinations = combinations(card_deck, 3)
triples_with_required_suit = filter(
    lambda card_triple: any(required_suit == suit for nominal, suit in card_triple),
    triples_combinations
)
triples = [', '.join(f'{nominal} {suit_cases[suit]}' for nominal, suit in triple) for triple in
           triples_with_required_suit]

triples.sort()
print(*triples[:10], sep='\n')
