# 1. Создайте список из N натуральных чисел(0 до N), упорядоченных по возрастанию. Среди чисел не хватает  
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1] пример - (1, 2, 4, 5, 6) Найдите это число (по примеру будет - 3)

from random import choice
	
def any_list(num):
	a_list = list(range(num+1)) # создаем список
	a_list.remove(choice(a_list)) # choice берет один случайный элемент из списка, remove - удаляет выбранный элемент
	return a_list
	
def find(n_list):
	for i in range(1, len(n_list)): # пробегаемся по списку
	    if n_list[i] -1 != n_list[i-1]: 
	        return n_list[i] -1
    
    
data = any_list(int(input("Введите число: ")))
print(data)
number = find(data)
print(number)
    
	
	
