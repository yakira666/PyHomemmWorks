"""
ЗАДАЧА:
Вводится список чисел в одну строку разделенные пробелом.
Определите, сколько в нем встречается различных чисел.

Примечание: Задачу можно решить в одну строчку.
"""

print(len(set([nums := float(i) for i in input("Введите числа через пробелы: ").split()])))

"""
DEBUG
34 4.7 16 95 38 4.7 1.23 34 87 48 1.23 95 16 22 38 4.7
"""
