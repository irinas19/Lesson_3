# Цифры числа справа налево
# Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке,
# разделяя их пробелами или новыми строками.
# При решении этой задачи нельзя использовать строки, списки, массивы
# (ну и циклы, разумеется). Разрешена только рекурсия и целочисленная арифметика.

def rev(N):
    if N == 1:
        return 1
    print(N)
    return rev(N-1)

print(rev(6))