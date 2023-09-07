# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def create_progr(a, b, c):
    progression = []
    progression.append(a)
    el_next = a
    d_progr = b
    total_elts_progr = c
    i = 1
    while i < total_elts_progr:
        el_next = el_next + d_progr
        progression.append(el_next)
        i += 1
    
    return progression


el1_progr = int(input('Введите первый элемент прогрессии: '))
d_progr = int(input('Введите разность прогрессии: '))
total_elts_progr = int(input('Введите кол-во элементов прогрессии: '))

p = create_progr(el1_progr, d_progr, total_elts_progr)
print(p)

# progr = []
# progr.append(el1_progr)

# print(progr)

# el_next = el1_progr
# i = 1
# while i < total_elts_progr:
#     el_next = el_next + d_progr
#     progr.append(el_next)
#     i += 1

# print(progr)



