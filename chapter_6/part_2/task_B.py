# Длины всех слов по чётности
# В этот раз продумайте функцию length_stats, которая получает текст,
# а возвращает пару объектов Series со словами в качестве индексов и их длинами в качестве значений.
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
    odd_words = [word for word in sorted_words if len(word) % 2]
    even_words = [word for word in sorted_words if not len(word) % 2]
    odd_lengths = [len(word) for word in odd_words]
    even_lengths = [len(word) for word in even_words]

    return pd.Series(odd_lengths, odd_words, dtype='int64'), pd.Series(even_lengths, even_words, dtype='int64')
