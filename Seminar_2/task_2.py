# Создать список длины n, значения формируются по формуле 3k + 1  где k принимает значения от 1 до n включительно
#  3 ========>    [4,7,10]

num_list = []   #  создали пустой список
n = int(input())
for k in range(1, n+1):
    num_list.append(3*k+1)                          # append метод который добавляет новые значения в конец списка
print(num_list)



