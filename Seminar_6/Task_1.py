# Напишите программу вычисления арифметического
	# выражения заданного строкой. Используйте операции
	# +,-,/,* приоритет операций стандартный. 
	# * Добавьте скобки,  приоритет операций меняется.

# exp = "4 * 3 - 1 / 9 - 7 * -1".split()
# exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

def sort_s(string):
    spl = string.split() # разделять по пробелам 
    fn_spl = []
    i = 0
    while i < len(spl):
        if spl[i] == "(": # нашли первую открвающ скобку
            bracket = spl.index(")") # нашли закрывающ скобку
            fn_spl.append(spl[i+1:bracket]) # взяли срез того что находится в скобках (сделали подсписок в списке)
            i = bracket
        else:
            fn_spl.append(spl[i]) # сложили все значения которые вне скобок
        i += 1
    return fn_spl


def calc(any_list):
    for i, v in enumerate(any_list):
        if isinstance(v, list): # проверка значений на определенный тип данных (нам нужен list)
            any_list[i] = calc(v)
    ch = [i for i, v in enumerate(any_list) if v in '*/']
    while ch:
        sm = ch[0]
        a, b, c = any_list[sm-1 : sm+2]
        any_list.insert(sm-1, actions[b] (a,c))
        del any_list[sm : sm+3]
        ch = [i for i, v in enumerate(any_list) if v in '*/']
    while len(any_list) > 1:
        a, b, c = any_list[:3]
        del any_list[:3]
        any_list.insert(0, actions[b] (a,c))
    return any_list[0]

d = input("Введите цифры: ")
print(sort_s(d))
print(calc(sort_s(d)))

