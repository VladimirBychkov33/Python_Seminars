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

if list_len >= pos_1 > 0 and list_len >= pos_2 > 0:         # не смог придумать, как задать условия не корректности (т.е. вне списка)
    print(numbers[pos_1 - 1] * numbers[pos_2 - 1])
else:
    print("There are no values for these indexes!")







    





