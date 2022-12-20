# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

n = int(input())
pos_1 = int(input())
pos_2 = int(input())

numbers = list(range(-n, n+1))
print(numbers)
list_len = len(numbers)
pos_1 = numbers[pos_1 - 1]
pos_2 = numbers[pos_2 - 1]

if pos_1 < list_len > pos_2:         # не смог понять, как задать условия не корректности (т.е. вне списка)
    product = pos_1 * pos_2
    print(product)
else:
    print("There are no values for these indexes!")





    





