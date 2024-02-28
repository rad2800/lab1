# Лабораторная работа №1
Выполнила студентка БСТ2201 Родина Алина
## Описание работы

*Задание №1*

Вызвать функцию print() и передать туда строку Hello, World!

*Задание №2*

Написать генератор случайных матриц(многомерных), который принимает опциональные параметры m, n, min_limit, max_limit, где m и n указывают размер матрицы, а min_lim и max_lim - минимальное и максимальное значение для генерируемого числа.

*Задание №3*

Реализовать методы сортировки строк числовой матрицы в соответствии с заданием. Оценить время работы каждого алгоритма сортировки и сравнить его со временем стандартной функции сортировки. Испытания проводить на сгенерированных матрицах. 

## Выполнение

### Задание №1
Для того, чтобы выполнить задание, мы используем функцию print(), отвечающую за вывод. Выполнение задания №1 представлено в коде ниже:

```python
print("Hello, world!")
```

### Задание №2
Для выполнения необходимо подключить библиотеку random.

```python
import random
#Запрос пользовательского ввода для определения размеров матрицы и диапазона значений
user_m = int(input("Введите количество столбцов: "))
user_n = int(input("Введите количество строк: "))
user_min_limit = int(input("Введите минимальный элемент: "))
user_max_limit = int(input("Введите максимальный элемент: "))
#Создание матрицы с заданными размерами и случайными значениями
matrix = [[random.randint(user_min_limit, user_max_limit) for j in range(user_n)] for i in range(user_m)]
#Вывод матрицы на экран
for i in range(user_m):
    print(matrix[i])  # Вывод строки матрицы
```
### Задание №3
Для выполнения необходимо подключить библиотеки random и time для осуществления измерения времени.
Алгоритм сортировки выбором:
```python
import random
import time
# Запрос пользовательского ввода для определения размеров матрицы и диапазона значений
user_m = int(input("Введите количество столбцов "))  # Ввод количества столбцов
user_n = int(input("Введите количество строк "))  # Ввод количества строк
user_min_limit = int(input("Введите минимальный элемент "))  # Ввод минимального значения
user_max_limit = int(input("Введите максимальный элемент "))  # Ввод максимального значения
start_time = time.time()  # Засекаем время выполнения
# Генерация матрицы с заданными параметрами
matrix = [[random.randint(user_min_limit, user_max_limit) for j in range(user_n)] for i in range(user_m)]
# Функция сортировки выбором для строки матрицы
def selection(stroka):
    n_elementov = len(stroka)
for i in range(n_elementov-1):
    # Начинаем считать, что текущий элемент - минимальный
    min_element = i
    for j in range(i + 1, n_elementov):
        # Ищем минимальный элемент в оставшейся части массива
        if stroka[j] < stroka[min_element]:
            min_element = j
    # Меняем местами текущий элемент с найденным минимальным элементом
    stroka[i], stroka[min_element] = stroka[min_element], stroka[i]
# Сортировка каждой строки матрицы и их вывод
for stroka in matrix:
    selection(stroka)  # Сортировка строки
    print(stroka)  # Вывод отсортированной строки
print("--- {0} ms ---".format((time.time() - start_time)))  # Вывод времени выполнения
```
Сложность = О(m×n2)=O(1.25×108).
Алгоритм сортировки вставкой:
```python
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
    # Проходим по каждому элементу строки
    element = stroka[i]
    j = i - 1
    while j >= 0 and stroka[j] > element:
        # Пока не достигли начала строки и предыдущий элемент больше текущего
        stroka[j + 1] = stroka[j]
        j -= 1
    # Вставляем текущий элемент на правильное место в отсортированной части массива
    stroka[j + 1] = element
for stroka in matrix:
    vstavka(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))
'''
O(500×5002)=O(125000000) или O(1.25×108)O(1.25×108).
Алгоритм сортировки пузырьком
```python
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
# Внешний цикл для прохода по всем элементам массива, кроме последнего
for i in range(n_elementov-1):
    # Внутренний цикл для сравнения и перемещения элементов
    for j in range(0, n_elementov - i - 1):
        # Сравниваем текущий элемент с последующим
        if stroka[j] > stroka[j + 1]:
            # Если текущий элемент больше следующего, меняем их местами
            stroka[j], stroka[j + 1] = stroka[j + 1], stroka[j]  # Поменять местами элементы j и j+1
for stroka in matrix:
    bubbles(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))
```
O(5002×500)=O(125000000) или O(1.25×108)O(1.25×108).
Сортировка Шелла
```python
import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix=[[random.randint(user_min_limit, user_max_limit) for j in range (user_n)] for i in range(user_m)]
def shell(stroka):
  n_elementov = len(stroka)  # Получаем количество элементов в массиве stroka
  d = n_elementov // 2  # Инициализируем переменную d как половину длины массива
  
  while d > 0:  # Начинаем цикл, который будет выполняться, пока d больше нуля
      for i in range(d, n_elementov):  # Цикл для прохода по элементам массива начиная с d-го индекса
          j = i  # Инициализируем переменную j значением i
          while j >= d and stroka[j - d] > stroka[i]:  # Цикл для сравнения и перемещения элементов
              stroka[j] = stroka[j - d]  # Перемещаем элементы на расстояние d
              j -= d  # Уменьшаем j на d
          stroka[j] = stroka[i]  # Присваиваем элементу на позиции j значение элемента на позиции i
      d //= 2  # Уменьшаем шаг d вдвое
for stroka in matrix:
    shell(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))
```
O(5002×500)=O(125000000) или O(1.25×108)O(1.25×108).
Быстрая сортировка
```python
import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix = [[random.randint(user_min_limit, user_max_limit) for j in range(user_n)] for i in range(user_m)]
def short(stroka):
    if len(stroka) <= 1:  # Если длина массива меньше или равна 1, возвращаем массив
      return stroka
    less_key = []  # Инициализируем массив для элементов меньше или равных ключу
    more_key = []  # Инициализируем массив для элементов больше ключа
    key = stroka[0]  # Присваиваем переменной key значение первого элемента массива
    for x in stroka[1:]:  # Цикл для прохода по элементам массива начиная со второго
        if x <= key:  # Если текущий элемент меньше или равен ключу
            less_key.append(x)  # Добавляем его в массив less_key
        else:
            more_key.append(x)  # Иначе добавляем его в массив more_key
    return short(less_key) + [key] + short(more_key)  # Рекурсивно вызываем функцию short для массивов less_key и more_key, а затем объединяем результаты с ключом в один массив и возвращаем его
for stroka in matrix:
    stroka = short(stroka)
    print(stroka)
print("--- {0} ms ---".format((time.time() - start_time)))
```
O(500×500×log(500))≈O(1.625×107)
Турнирная сортировка
```python
import random
import time
user_m = int(input("Введите количество столбцов "))
user_n = int(input("Введите количество строк "))
user_min_limit = int(input("Введите минимальный элемент "))
user_max_limit = int(input("Введите максимальный элемент "))
start_time = time.time()
matrix = [[random.randint(user_min_limit, user_max_limit) for j in range(user_n)] for i in range(user_m)]
def sortm(stroka):
    if len(stroka) <= 1:  # Если длина массива меньше или равна 1, возвращаем массив
        return stroka
    mid = len(stroka) // 2  # Находим середину массива
    lefter = stroka[:mid]  # Делим массив на две части: левую
    righter = stroka[mid:]  # и правую
    lefter = sortm(lefter)  # Рекурсивно вызываем функцию sortm для левой части
    righter = sortm(righter)  # Рекурсивно вызываем функцию sortm для правой части
    return merge(lefter, righter)  # Объединяем отсортированные левую и правую части с помощью функции merge и возвращаем результат
def merge(left, right):
    result = []  # Инициализируем массив для объединенного результата
    left_index, right_index = 0, 0  # Устанавливаем начальные индексы для левого и правого массивов
    while left_index < len(left) and right_index < len(right):  # Пока не достигнут конец хотя бы одного из массивов
        if left[left_index] < right[right_index]:  # Если элемент из левого массива меньше элемента из правого
            result.append(left[left_index])  # Добавляем его в результат и увеличиваем индекс левого массива
            left_index += 1
        else:
            result.append(right[right_index])  # Иначе добавляем элемент из правого массива и увеличиваем индекс правого массива
            right_index += 1
    result.extend(left[left_index:])  # Добавляем оставшиеся элементы из левого массива в результат
    result.extend(right[right_index:])  # Добавляем оставшиеся элементы из правого массива в результат
    return result  # Возвращаем объединенный отсортированный результат
for i in range(len(matrix)):
    matrix[i] = sortm(matrix[i])
    print(matrix[i])
print("--- {0} ms ---".format((time.time() - start_time)))
```
O(500×500×log(500))≈O(1.625×107)
### Сравним время работы программы по результатам тестирования. Везде вводим матрицу 500*500, минимальный элемент 5, максимальный 5000
При сортировке выбором: 9.113574266433716 ms
При сортировке вставкой: 7.550020694732666 ms
При сортировке обменом (пузырьком): 17.050814628601074 ms
При сортировке Шелла: 1.0748920440673828 ms
При быстрой сортировке: 0.9554159641265869 ms
При турнирной сортировке: 1.5538842678070068 ms
Стандартная: 0.40781736373901367 ms

Самая быстрая, не считая стандартной, - быстрая, самая медленная - пузырьком
