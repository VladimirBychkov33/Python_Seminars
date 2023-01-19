# 2. Создайте список, в который попадают числа,
	#    описывающие возрастающую последовательность.
	#    Порядок элементов менять нельзя.

from random import choices

def any_list(num):
	    return choices(range(1, num+2), k=num) # создание списка из случайных повторяющихся чисел -[2, 9, 9, 3, 1, 5, 3, 3, 11, 9]

def seq(some_list):
    temp_list = [] # создание списка, куда будем складывать подсписки
    for i in range(len(some_list)): # пробегаемся по списку изначальному (внешней цикл)
        num_1 = some_list[i]
        out_list = [num_1] # создание подсписка 
        for j in range(i+1, len(some_list)): # пробегаемся по списку изначальному (внутренний цикл)
            if some_list[j] > num_1:
                num_1 = some_list[j]
                out_list.append(num_1)
        if len(out_list) > 1: # если длина подсписка больше 1 элемента
            temp_list.append(out_list)
    return temp_list

a = any_list(10)
print(a) 
print(seq(a))