# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 17:35:27 2025

@author: Home
"""
import random

#размер списка
size = 10

#Создание списка со случайными числами
array = [random.randint(1, 10) for _ in range(size)]
print(array)

sum = 0

#Нахождение суммы всех четных чисел в списке
for i in array:
    if i%2==0:
        sum+=i
        
print(sum)