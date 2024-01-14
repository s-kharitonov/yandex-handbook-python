# Ключевой секрет
# Вася любит секреты и шифрование.
# Он часто пользуется шифром на основе замен и просит разработать вас функцию,
# которая позволит ему быстро шифровать сообщения.
#
# Напишите функцию secret_replace, которая принимает:
#
# текст требующий шифрования;
# именованные аргументы — правила замен, представляющие собой кортежи из одного или нескольких значений.
# Функция должна вернуть зашифрованный текст.
#
# Примечание
# Ваше решение должно содержать только функции.
# В решении не должно быть вызовов требуемых функций.

def secret_replace(text, **rules):
    result = ''
    rules = {letter: {'replacements': replacements, 'replace_count': 0} for letter, replacements in rules.items()}
    for letter in text:
        if letter in rules:
            letter_replacements = rules[letter]
            replacements = letter_replacements['replacements']
            replace_count = letter_replacements['replace_count']
            replace = replacements[replace_count % len(replacements)]

            result += replace
            letter_replacements['replace_count'] += 1
        else:
            result += letter
    return result
