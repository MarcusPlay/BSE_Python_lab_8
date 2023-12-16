#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В начале кортежа записано несколько равных между собой элементов. Определить
# количество таких элементов и вывести все элементы, следующие за последним из них.
# Рассмотреть возможность того, что весь массив заполнен одинаковыми элементами.

if __name__=="__main__":
    t = tuple(map(int, input("Введите кортеж значений через пробел: ").split()))
    
    elements = t

    equal_elements = 0
    following_elements = []

    for current, next_element in zip(elements, elements[1:]):
        if current == next_element:
            equal_elements += 1
        elif equal_elements > 0:
            following_elements.append(next_element)

    print(f"Количество равных элементов: {equal_elements + 1}")
    print("Следующие за последним из них элементы:", following_elements)

