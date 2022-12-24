# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample      

def get_list (amount):
    new_list = sample(range(1,amount+1), k=amount)  
    return new_list

def product_pair (some_list):
    list_user = []
    list_len = len(some_list)

    for i in range(list_len // 2):         
        list_user.append(some_list[i] * some_list[list_len - i - 1])
  
    if list_len % 2:
        list_user.append(some_list[list_len // 2])
    return list_user
    
list_1 = get_list(int(input("Введите число: ")))
print(list_1)
print(product_pair(list_1)) 