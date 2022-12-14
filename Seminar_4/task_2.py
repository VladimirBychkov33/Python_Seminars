# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
  #    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
  #    Уравнения и корни запишите в файл.
from math import sqrt

def find_r(a, b, c):
        D = b**2 - 4*a*c  # формула дискрименанта
        with open("Diskr.txt", "a", encoding="utf-8") as my_f: # создание файла с именем и указанием расширения - Diskr.txt
                                                               # "a" - означает что будем дозаписывать(добавлять) в файл
                                                               # encoding="utf-8" - кодировка, она нужна если данные комбинированные(кирилица и латиница)
                                                               # my_f - это переменная с данным файлом
            my_f.write(f"{a}x² + {b}x + {c} = 0\n")            # write - то что будем дозаписывать, \n - переход на новую строку
            if D > 0:
                x1 = (-b - sqrt(D)) / (2*a)
                x2 = (-b + sqrt(D)) / (2*a)
                my_f.write(f"{x1, x2}\n")
            elif D == 0:
                x = -b / (2*a)
                my_f.write(f"{x}\n")
            else:
                my_f.write("нет корней\n")

find_r(3, 8, 12)

# Второй вариант:

# from math import sqrt


# def roots_equ(a, b, c):
#     d = b ** 2 - 4 * a * c
#     with open("roots.txt", "a", encoding="utf-8") as my_f:
#         my_f.write(f"{a}x ** 2 + {b}x + {c}\n")
#         if d > 0 and a:
#             my_f.write(f"The first root: {(-b + sqrt(d)) / (2 * a):.2f}\n")
#             my_f.write(f"The first root: {(-b - sqrt(d)) / (2 * a):.2f}\n")
#         elif d == 0 and a:
#             my_f.write(f"The root: {-b / (2 * a):.2f}\n")
#         else:
#             my_f.write("There are no roots.\n")


# # 1 2 -3, 5 6 -7, 8 9 -10
# for i in range(3):
#     roots_equ(int(input("Enter the coefficient 'a': ")), int(input("Enter the coefficient 'b': ")),
#               int(input("Enter the coefficient 'c': ")))

