# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

from decimal import Decimal, ROUND_HALF_UP

n = input("Enter a real number: ")
m = input("Enter the required accuracy '0.0001': ")
number = Decimal(n)
print(number.quantize(Decimal(m), ROUND_HALF_UP))

# Пометки для себя:
# ROUND_HALF_EVEN: округление происходит до ближайшего четного числа, если округляемая часть равна 5
# ROUND_HALF_DOWN: округляет число в сторону повышения, если после него идет число больше 5
# ROUND_05UP: округляет 0 до единицы, если после него идет число 5 и выше
# ROUND_CEILING: округляет число в большую сторону вне зависимости от того, какое число идет после него
# ROUND_FLOOR: не округляет число вне зависимости от того, какое число идет после него