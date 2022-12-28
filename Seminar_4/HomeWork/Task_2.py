# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]

num = int(input("Enter the number: "))
some_list = []
temp = 2
while num > 1:
    if num % temp == 0:
        some_list.append(temp)
        num = num / temp
    else:
        temp = temp + 1
print(some_list)

