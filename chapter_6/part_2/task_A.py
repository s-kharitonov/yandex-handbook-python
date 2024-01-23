# Длины всех слов - 2
# Напишите функцию length_stats, которая получает текст,
# а возвращает объект Series со словами в качестве индексов и их длинами в качестве значений.
#
# Все слова в тексте предварительно переведите в нижний регистр, избавьтесь от знаков препинания и цифр,
# а также отсортируйте в лексикографическом порядке.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.
import pandas as pd


def length_stats(text):
    letters_with_spaces = filter(lambda letter: letter.isalpha() or letter.isspace(), text.lower())
    words = set(''.join(letters_with_spaces).split())
    sorted_words = sorted(words)
    return pd.Series(list(map(lambda word: len(word), sorted_words)), sorted_words)
