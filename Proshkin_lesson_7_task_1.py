"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

import random

lst = [random.randrange(-100, 100, 1) for _i in range(30)]
print('Исходный массив:\n', lst)

def babble_sort(array):
    n = len(array)
    not_ordered = True
    while not_ordered:
        not_ordered = False # Частично сократит число внешних итераций
        for i in range(n): # Оптимизация, позволяющая сократить число внутренних итераций в 2 раза
            index = len(array) - i - 1
            if array[index] > array[index - 1]:
                array[index - 1], array[index] = array[index], array[index - 1]
                not_ordered = True
        n -= 1
    return array

print('Отсортированный масив:\n', babble_sort(lst))

# Тестовое изменение 1

# Тестовое изменение 1.1

# Тестовое изменение 1.2
