# Друзья друзей
# Теория шести рукопожатий — социологическая теория,
# согласно которой любые два человека на Земле разделены не более,
# чем пятью уровнями общих знакомых (и, соответственно, шестью уровнями связей).
# Формальная математическая формулировка теории: диаметр графа знакомств не превышает 6.
# Мы не станем так сильно углубляться в дружественные связи и пока нам хватит только двух уровней.
# Напишите программу, которая по списку дружественных пар для каждого человека определяет список «друзей 2-го уровня».
#
# Формат ввода
# В каждой строке записывается два имени.
# Окончанием ввода служит пустая строка.
#
# Формат вывода
# Выведите список всех людей и их «друзей 2-го уровня» в формате «Человек: Друг1, Друг2, ...».
# Список людей и друзей в каждой строке требуется вывести в алфавитном порядке без повторений.
friends_by_name = dict()

while friends_pair := input():
    friends = friends_pair.split()
    first_human = friends[0]
    second_human = friends[1]
    first_human_friends = friends_by_name.get(first_human, set())
    second_human_friends = friends_by_name.get(second_human, set())

    first_human_friends.add(second_human)
    second_human_friends.add(first_human)
    friends_by_name[first_human] = first_human_friends
    friends_by_name[second_human] = second_human_friends

for name, friends in sorted(friends_by_name.items()):
    second_level_friends = set()

    for friend_name in friends_by_name[name]:
        for second_level_friend_name in friends_by_name[friend_name]:
            if second_level_friend_name != name and second_level_friend_name not in friends:
                second_level_friends.add(second_level_friend_name)

    print(f'{name}: {", ".join(sorted(second_level_friends))}')

