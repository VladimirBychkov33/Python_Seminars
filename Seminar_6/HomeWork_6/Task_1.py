# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых 
# больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample      

temp = sample(range(30), k=10)
print(temp)

res_list = [temp[i] for i in range(1,len(temp)) if temp[i] > temp[i-1]]
print(res_list)





