# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample 

def words_list (num, word="абв"): 
                                  
    w_list = []
    if num >= 1: 
        for i in range(num):
            m = sample(word, k=3) 
            w_list.append("".join(m)) 
        return " ".join(w_list)
    else:
        return "The data is incorrect"

def delete_str (any_str):
    return " ".join(i for i in any_str.split() if i != "абв")
 
user_num = int(input('Введите число: '))
temp = words_list(user_num)
print(temp)
print(delete_str(temp))
