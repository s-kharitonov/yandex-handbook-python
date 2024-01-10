# Это будет наш секрет
# Шифр Цезаря, также известный как шифр сдвига, код Цезаря — один из самых простых
# и наиболее широко известных методов шифрования.
# Он назван в честь римского полководца Гая Юлия Цезаря, использовавшего его для секретной
# переписки со своими генералами.
#
# Давайте реализуем эту систему шифрования. Однако для простоты мы будем сдвигать только латинские символы по кругу.
#
# Формат ввода
# Вводится размер сдвига для шифрования.
#
# В файле public.txt содержится текст на английском языке.
#
# Формат вывода
# В файл private.txt запишите зашифрованный текст.
shift_size = int(input())
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

with open('public.txt', 'r', encoding='UTF-8') as public_file:
    result = ''
    for char in public_file.read():
        if not char.isalpha():
            result += char
            continue
        shifted_char = alphabet[(ord(char.lower()) - ord('a') + shift_size) % len(alphabet)]
        result += shifted_char.upper() if char.isupper() else shifted_char
with open('private.txt', 'w', encoding='UTF-8') as private_file:
    print(result, file=private_file)
