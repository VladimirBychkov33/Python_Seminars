# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

def check():
    enter_list = input("Введите числа через пробел").split()
    right_list = []
    for i in range(len(enter_list)):
        enter_list[i] = enter_list[i].strip("!,;") # метод strip убирает пробелы и символы 
        if enter_list[i].isdigit:  # проверка, содержит ли строка символы цифр
            right_list.append(enter_list[i])  # получение списка
    print(right_list)
    return right_list

def max_min_finder(any_list):
    if any_list:
        return max(any_list, key=int), min(any_list, key=int)  # key=int - что бы воспринимал строковый элемент как целочисленный
    return []

print(*max_min_finder(check()))

# второй вариант решения:

# def check(str_list: list):      # проверяющая функция 
#     new_list = []
#     for i, num in enumerate(str_list):
#         str_list[i] = num.strip('.,;:?!')   # метод strip убирает пробелы и символы (в начале и в конце строки, но не в центре), 
#                                              # которые мы укажем в скобках
#         if str_list[i].replace("-", "").isdigit():
#             new_list.append(str_list[i])
#     return new_list    

# def find_max_min(nums_str: str):
#     list_nums = nums_str.split()
#     right_list = check(list_nums)

#     if right_list:
#         return min(right_list, key=int), max(right_list, key=int)
#     print("The data is incorrect")
#     return []

# print(*find_max_min(input("Enter the numbers separated by a space: ")))