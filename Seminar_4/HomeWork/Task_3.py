# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
#  неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []

from random import randint

def get_list(len_list: int) -> list:
    numbers = []
    for i in range(len_list):
        numbers.append(randint(1, 6))         # создание произвольного списка с повторяющимися значениями
    if len_list < 0:
        print("Negative value of the number of numbers!")
    return numbers

def delete_same_numbers(some_list: list):
    result_list = []
    for i in range(len(first_list)):
        count = first_list.count(first_list[i])
        if count == 1:
            result_list.append(first_list[i])
    print(result_list)

first_list = get_list(int(input("Enter length of a list: ")))
print(first_list)
delete_same_numbers(first_list)

