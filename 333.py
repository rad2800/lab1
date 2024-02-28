#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, world!")


# In[16]:


import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
matrix=[[random.randint(user_min_limit, user_max_limit) for j in range (user_n)] for i in range(user_m)]
for i in range(user_m):
    print(matrix[i])


# In[21]:


import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix=[[random.randint(user_min_limit, user_max_limit) for j in range (user_n)] for i in range(user_m)]
def selection(stroka):
    n_elementov = len(stroka)
    for i in range(n_elementov-1):
        min_element = i
        for j in range(i + 1, n_elementov):
            if stroka[j] < stroka[min_element]:
                min_element = j
        stroka[i], stroka[min_element] = stroka[min_element], stroka[i]
for stroka in matrix:
    selection(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))


# In[22]:


import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix=[[random.randint(user_min_limit, user_max_limit) for j in range (user_n)] for i in range(user_m)]
def vstavka(stroka):
    for i in range(len(stroka)):
        element = stroka[i]
        j = i - 1
        while j >= 0 and stroka[j] > element:
            stroka[j + 1] = stroka[j]
            j -= 1
        stroka[j + 1] = element

for stroka in matrix:
    vstavka(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))


# In[23]:


import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix=[[random.randint(user_min_limit, user_max_limit) for j in range (user_n)] for i in range(user_m)]
def bubbles(stroka):
    n_elementov = len(stroka)
    for i in range(n_elementov-1):
        for j in range(0, n_elementov - i-1):
            if stroka[j] > stroka[j + 1]:
                stroka[j], stroka[j + 1] = stroka[j + 1], stroka[j]
for stroka in matrix:
    bubbles(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))


# In[24]:


import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix=[[random.randint(user_min_limit, user_max_limit) for j in range (user_n)] for i in range(user_m)]
def shell(stroka):
    n_elementov = len(stroka)
    d = n_elementov // 2
    while d > 0:
        for i in range(d, n_elementov):
            j = i
            while j >= d and stroka[j - d] > stroka[i]:
                stroka[j] = stroka[j - d]
                j -= d
            stroka[j] = stroka[i]
        d //= 2
for stroka in matrix:
    shell(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))


# In[25]:


import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix = [[random.randint(user_min_limit, user_max_limit) for j in range(user_n)] for i in range(user_m)]
def short(stroka):
    if len(stroka) <= 1:
        return stroka
    less_key = []
    more_key = []
    key = stroka[0]
    for x in stroka[1:]:
        if x <= key:
            less_key.append(x)
        else:
            more_key.append(x)
    return short(less_key) + [key] + short(more_key)
for stroka in matrix:
    stroka = short(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))


# In[26]:


import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix = [[random.randint(user_min_limit, user_max_limit) for j in range(user_n)] for i in range(user_m)]
def sortm(stroka):
    if len(stroka) <= 1:
        return stroka
    mid = len(stroka) // 2
    lefter = stroka[:mid]
    righter = stroka[mid:]
    lefter = sortm(lefter)
    righter = sortm(righter)
    return merge(lefter, righter)
def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result
for i in range(len(matrix)):
    matrix[i] = sortm(matrix[i])
    print(matrix[i])
print("--- {0} ms ---".format((time.time() - start_time)))


# In[28]:


import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix = [[random.randint(user_min_limit, user_max_limit) for j in range(user_n)] for i in range(user_m)]
matrix.sort()
print("--- {0} ms ---".format((time.time() - start_time)))


# In[ ]:




