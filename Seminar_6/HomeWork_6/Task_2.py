# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

def find_digit (num):
    res_list = [i for i in range(20, num+1) if i % 20 == 0 or i % 21 == 0]
    return res_list

print(find_digit(int(input('Enter number: '))))
