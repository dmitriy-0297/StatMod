import numpy as np

template = '11111'
m = 5 #размер шаблона
n = 100 #размер выборки
M = 20 #size подподвыборки
N = int(n // M) #количество подпоследовательностей
#исходные параметры

numbers = []
for i in range(0, n):
    num = np.random.uniform(0, 1)
    if num < 0.5:
        numbers.append(0)
    elif num >= 0.5:
        numbers.append(1)
#формируем начальный массив

numbersDiv = [] #массив разбиений
tmp = 0 #для движения по массиву
for i in range(0, N):
    numbersDiv.append([])
    for j in range(0, M):
        numbersDiv[i].append(numbers[tmp])
        #print(i, " ", numbersDiv[i])
        tmp += 1
#имеем разбитый массив

v = 0 #количество совпадений с шаблоном
array_v = [] #массив совпадений
for i in range(0, N):
    array_v.append(v)
for i in range(0, N):
    j = 0
    str_Num = str(numbersDiv[i][j]) + str(numbersDiv[i][j + 1]) + str(numbersDiv[i][+2]) + str(numbersDiv[i][j+3]) + str(numbersDiv[i][j + 4])
    if str_Num == template:
        array_v[i] += 1
        j += 1
        str_Num = ""
    else:
        j += 1
        str_Num = ""
#сверям с шаблоном

miu = (M - m + 1) / (pow(2, m))
print("miu ", miu)
dev = M * ((1 / (pow(2, m))) - ((2 * m - 1) / (pow(2, (2 * m)))))
print("deviation^2", dev)
hi = 0
for i in range(1, N):
    hi += ((pow((array_v[i] - miu), 2)) / dev)
print("degree of freedom: ", (N -1))
print("hi^2 ", hi)
#считаем статистику
