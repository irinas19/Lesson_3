# 2. Напишите программу на Python, которая принимает два списка ключей и значений и
# создает словарь, используя эти списки. Если длины списков не совпадают, программа
# должна выводить сообщение об ошибке.
#
# Пример входных данных:
# keys = ['name', 'age', 'gender']
# values = ['John', 25, 'male']
#
# Пример выходных данных:
# {'name': 'John', 'age': 25, 'gender': 'male'}

keys = list(input())
values = list(input())
if len(keys) != len(values):
    print('Ошибка')
for i in values:
    d = {}
    for j in range(len(keys)):
        d[keys[j]] = values[j]
print(d)
