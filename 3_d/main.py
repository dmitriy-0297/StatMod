import random
import numpy as np
import math

def RNEXP(b):
    u = random.random()
    r = -b * np.log(u)
    return r


def exponentDist():
    arrayExp = []
    sizeArray = 20
    for i in range(1, sizeArray):
        arrayExp.append(RNEXP(1))
    x = (np.unique(arrayExp))
    Fi = []
    Ei = []
    Di = []
    from numpy import mean, std
    M = mean(arrayExp)
    S = std(arrayExp)
    for i in range(0, len(arrayExp)):
        Fi.append(i/len(arrayExp))
        Ei.append(1 + math.erf((x[i]-M)/(math.sqrt(2*S**2)))/2)
        Di.append(abs(Fi[i]-Ei[i])/3)
    print('x[i]')
    for i in range(1, len(arrayExp)):
       print(x[i])
    print('Fi[i]')
    for i in range(1, len(arrayExp)):
        print(Fi[i])
    print('Ei[i]')
    for i in range(1, len(arrayExp)):
        print(Ei[i])
    print('Di[i]')
    for i in range(1, len(arrayExp)):
        print(Di[i])
    print('Наблюдаемое значение критерия D = ', max(Di))
    print(f'Число степеней свободы n = {len(arrayExp)}')
    pass


exponentDist()
