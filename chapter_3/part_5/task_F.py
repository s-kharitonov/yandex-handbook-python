# Транслитерация 2.0
# Для международных документов русский текст преобразуется с использованием латинского алфавита.
# ГОСТ Р 52535.1-2006 задаёт правила транслитерации идентификационных карт.
# Ниже приведена таблица замен:
#
# А — A
# Б — B
# В — V
# Г — G
# Д — D
# Е — E
# Ё — E
# Ж — ZH
# З — Z
# И — I
# Й — I
# К — K
# Л — L
# М — M
# Н — N
# О — O
# П — P
# Р — R
# С — S
# Т — T
# У — U
# Ф — F
# Х — KH
# Ц — TC
# Ч — CH
# Ш — SH
# Щ — SHCH
# Ы — Y
# Э — E
# Ю — IU
# Я — IA
# Давайте транслитерируем русский текст.
# Букву «ё» транслитерируйте как «e», «й» как «и», а «ъ» и «ь» (и их заглавные версии «Ъ» и «Ь»)
# должны исчезнуть из текста.
# Строчные буквы заменяются на строчные, заглавные заменяются на заглавные.
# Если заглавная буква превращается при транслитерации в несколько букв,
# то заглавной должна остаться только первая из них (например, «Ц» → «Tc»).
# Все некириллические символы должны остаться на месте.
#
# Формат ввода
# В одной папке с вашей программой лежит файл cyrillic.txt.
# В нём, в числе прочих, содержится некоторое количество кириллических символов.
#
# Формат вывода
# В файл transliteration.txt записать результат транслитерации исходного файла.
LETTERS_BY_TRANSLITERATED_LETTER = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TC',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA'
}

with open('cyrillic.txt', 'r', encoding='UTF-8') as file_in, open('transliteration.txt', 'w',
                                                                  encoding='UTF-8') as file_out:
    result = ''

    for symbol in file_in.read():
        if symbol.isascii() or symbol.isspace():
            result += symbol
            continue

        upper_symbol = symbol.upper()

        if upper_symbol == 'Ъ' or upper_symbol == 'Ь':
            continue

        transliterated_symbol = LETTERS_BY_TRANSLITERATED_LETTER.get(upper_symbol, '')

        if symbol.islower():
            result += transliterated_symbol.lower()
        else:
            result += transliterated_symbol[0] + transliterated_symbol[1::].lower()

    print(result, file=file_out)
