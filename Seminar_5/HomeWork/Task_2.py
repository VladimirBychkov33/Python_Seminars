# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

open('text_words.txt', 'a', encoding='UTF-8') 
    
with open('text_words.txt', 'r') as data:
    any_str = data.readline()
   
def encod(some_str):
    encond = ''
    prev_char = ''
    count = 1
    if not some_str:
        return ''

    for char in some_str:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


res = encod(any_str)
print(res)
