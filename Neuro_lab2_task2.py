# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 17:47:12 2025

@author: Home
"""

import pandas as pd # библиотека pandas нужна для работы с данными
import numpy as np # numpy для работы с векторами и матрицами

# Считываем данные 

df = pd.read_csv('data.csv')

y = df.iloc[:, 4].values
y = np.where(y == "Iris-setosa", 1, -1)

X = df.iloc[:, [0,1,2]].values

# функция нейрона:
def neuron(w,x):
    if((w[1]*x[0]+w[2]*x[1]+w[3]*x[2]+w[0])>=0):
        predict = 1
    else: 
        predict = -1
    return predict


# зададим начальные значения весов
w = np.random.random(4)
eta = 0.01  # скорость обучения

for xi, target, j in zip(X, y, range(X.shape[0])):
    predict = neuron(w,xi)   
    w[1:] += (eta * (target - predict)) * xi
    w[0] += eta * (target - predict)
    print(w)
        
        
sum_err = 0
for xi, target in zip(X, y):
    predict = neuron(w,xi) 
    sum_err += (target - predict)/2

print("Всего ошибок: ", sum_err)