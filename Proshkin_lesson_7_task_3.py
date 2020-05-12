"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""

import random
lst = [random.randrange(0, 100, 1) for _i in range(15)]

def gnome_sort(lst):
    array = lst.copy()
    def _gnome_rec(array, i=0, j=None):
        if j is None:
            j = len(array) - 1
        if array[j] < array[i]:
            array[i], array[j] = array[j], array[i]
        if j - i > 1:
            t = (j - i + 1) // 3
            _gnome_rec(array, i, j - t)
            _gnome_rec(array, i + t, j)
            _gnome_rec(array, i, j - t)
        return array

    return _gnome_rec(array, 0, len(array) - 1)

def median(ns_array):
    lenght = len(ns_array)
    if lenght % 2 == 0:
        return 'Для четного массива медианы нет'
    s_array = gnome_sort(ns_array)
    middle = (lenght - 1) // 2

    index = ns_array.index(s_array[middle])
    return f'Индекс: {index} , значение: {s_array[middle]}'

print('Медиана:\n', median(lst))
print('Исходный массив:\n', lst)
print('Отсортированный масив:\n', gnome_sort(lst))