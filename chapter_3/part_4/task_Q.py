# А есть ещё варианты?
# Давайте вновь поможем Виталию выяснить, какие вариации вытащить из колоды определённые тройки карт возможны.
# Напишите программу, которая выводит список вариантов согласно требованиям.
#
# Формат ввода
# В первой строке записана масть, которая должна присутствовать в тройке.
# Во второй строке записан достоинство, которого не должно быть в тройке.
# В третьей строке записан предыдущий вариант полученный Виталием.
#
# Формат вывода
# Выведите следующий вариант расклада.
from itertools import product, combinations

suit_cases = {
    'буби': 'бубен',
    'пики': 'пик',
    'трефы': 'треф',
    'черви': 'червей',
}
required_suit = input()
nominal_for_remove = input()
prev_triple = input()
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

for i, triple in enumerate(triples):
    if prev_triple == triple:
        print(triples[i + 1])
        break
