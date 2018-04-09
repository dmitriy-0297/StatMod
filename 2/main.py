import numpy as np
import matplotlib.pyplot as plt
import random as random_number
import random
import math

def IRNLOG(p):
    alpha = random.random()
    p_it = -(1/math.log(p))*(1-p)
    m = 1
    while (alpha - p_it) >= 0:
        alpha = alpha - p_it
        p_it = p_it * (m / (m + 1)) * (1 - p)
        m = m + 1
    return m


def logDistribution():
    print("\n")
    print("Log distribution")
    sizeArray = int(input("Enter Array Size: "))
    p = float(input("Enter p: "))
    arrayLog = []
    for i in range(1, sizeArray):
        arrayLog.append(IRNLOG(p))
    from numpy import mean, var
    m = mean(arrayLog)  # мат. одидание
    print("mean = ", m)
    v = var(arrayLog)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayLog) / float(len(arrayLog))
    amounts, bins, _ = plt.hist(arrayLog, weights=weights)
    plt.savefig('denstFunctLog.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctLog.png')

def IRNPSN(mu):
    if mu < 88:
        alpha = random.random()
        p_it = alpha
        m = 1
        while p_it >= math.exp(-mu):
            alpha = random.random()
            p_it = p_it*alpha
            m = m + 1
    else:
        m = random_number.normalvariate(mu, mu)
    return m


def IRNPOI(mu):
    if mu < 88:
        alpha = random.random()
        p_it = math.exp(-10)
        m = 1
        while (alpha - p_it) >= 0:
            alpha = alpha - p_it
            p_it = p_it*(mu/m)
            m = m+1
    else:
        m = random_number.normalvariate(mu, mu)
    return m

def puasonDistribution():
    print("\n")
    print("Puason distribution")
    sizeArray = int(input("Enter Array Size: "))
    mu = float(input("Enter mu: "))
    arrayPuason = []
    for i in range(1, sizeArray):
        arrayPuason.append(IRNPOI(mu))
    from numpy import mean, var
    print("IRNPOI")
    m = mean(arrayPuason)  # мат. одидание
    print("mean = ", m)
    v = var(arrayPuason)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayPuason) / float(len(arrayPuason))
    amounts, bins, _ = plt.hist(arrayPuason, weights=weights)
    plt.savefig('denstFunctPuasom_IRNPOI.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctPuasom_IRNPOI.png')
    arrayPuason.clear()
    for i in range(1, sizeArray):
        arrayPuason.append(IRNPSN(mu))
    from numpy import mean, var
    print("IRNPSN")
    m = mean(arrayPuason)  # мат. одидание
    print("mean = ", m)
    v = var(arrayPuason)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayPuason) / float(len(arrayPuason))
    amounts, bins, _ = plt.hist(arrayPuason, weights=weights)
    plt.savefig('denstFunctPuasom_IRNPSN.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctPuasom_IRNPSN.png')

def IRNGEO_1(p):
    alpha = random.random()
    p_it = p
    m = 0
    while (alpha - p_it) >= 0:
        alpha = alpha - p_it
        p_it = p_it*(1-p)
        m = m + 1
    return m

def IRNGEO_2(p):
    alpha = random.random()
    k = 0
    while alpha > p:
        alpha = random.random()
        k = k + 1
    return k

def IRNGEO_3(p):
    alpha = random.random()
    m = round(math.log(alpha)/math.log(1-p))+1
    return m

def geomDistribution():
    print("\n")
    print("Geometric distribution")
    sizeArray = int(input("Enter Array Size: "))
    p = float(input("Enter p: "))
    arrayGeom = []
    for i in range(1, sizeArray):
        arrayGeom.append(IRNGEO_1(p))
    from numpy import mean, var
    print("IRNGEO_1")
    m = mean(arrayGeom) # мат. одидание
    print("mean = ", m)
    v = var(arrayGeom) # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayGeom) / float(len(arrayGeom))
    amounts, bins, _ = plt.hist(arrayGeom, weights=weights)
    plt.savefig('denstFunctGeom_1.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctGeom_1.png')
    arrayGeom.clear()
    for i in range(1, sizeArray):
        arrayGeom.append(IRNGEO_2(p))
    print("IRNGEO_2")
    from numpy import mean, var
    m = mean(arrayGeom)  # мат. одидание
    print("mean = ", m)
    v = var(arrayGeom)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayGeom) / float(len(arrayGeom))
    amounts, bins, _ = plt.hist(arrayGeom, weights=weights)
    plt.savefig('denstFunctGeom_2.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctGeom_2.png')
    arrayGeom.clear()
    for i in range(1, sizeArray):
        arrayGeom.append(IRNGEO_3(p))
    from numpy import mean, var
    print("IRNGEO_3")
    m = mean(arrayGeom)  # мат. одидание
    print("mean = ", m)
    v = var(arrayGeom)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayGeom) / float(len(arrayGeom))
    amounts, bins, _ = plt.hist(arrayGeom, weights=weights)
    plt.savefig('denstFunctGeom_3.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctGeom_3.png')
    pass


def IRNBIN(n, p):
    if n >= 100:
        m = round(random_number.normalvariate(n * p, math.sqrt(n * p * (1.0 - p))) + 0.5)
    else:
        alpha = random.random()
        p_it = pow((1 - p), n)
        m = 0
        while (alpha - p_it) >= 0:
            alpha = alpha - p_it
            p_it = p_it * (p * (n - m)) / ((m + 1) * (1 - p))
            m = m + 1
    return m

def binomialDistribution():
    print("\n")
    print("Binomial distribution")
    sizeArray = int(input("Enter Array Size: "))
    N = int(input("Enter N: ")) #количество испытаний
    p = float(input("Enter p: ")) #вероятность успеха при одном испытании
    arrayBinomial = []
    for i in range(1, sizeArray):
        arrayBinomial.append(IRNBIN(N, p))
    from numpy import mean, var
    m = mean(arrayBinomial)  # мат. одидание
    print("mean = ", m)
    v = var(arrayBinomial)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayBinomial) / float(len(arrayBinomial))
    amounts, bins, _ = plt.hist(arrayBinomial, weights=weights)
    plt.savefig('denstFunctBinom.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctBiom.png')
    pass

def distribution(amounts, bins):
    amounts = np.insert(amounts, 0, 0.)
    n = sum(amounts)
    return [sum(amounts[:i + 1]) / n for i, bin in enumerate(bins)]


def numUniformDistribution(r_low, r_up):
    r = ((r_up - r_low + 1) * np.random.uniform(0, 1) + r_low)
    return r

def uniformDistribution():
    print("Uniform distribution")
    sizeArray = int(input("Enter Array Size: "))
    r_low = int(input("Enter r_low: "))
    r_up = int(input("Enter r_up: "))
    arrayUnifDist = []
    for i in range(0, sizeArray):
        arrayUnifDist.append(numUniformDistribution(r_low, r_up))
    from numpy import mean, var
    m = mean(arrayUnifDist)  # мат. одидание
    print("mean = ", m)
    v = var(arrayUnifDist)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayUnifDist) / float(len(arrayUnifDist))
    amounts, bins, _ = plt.hist(arrayUnifDist, weights=weights)
    plt.savefig('denstFunctUniform.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctUniform.png')
    pass


uniformDistribution() #равномерное распределение
binomialDistribution() #биномиальное распределение
geomDistribution() #геометрическое распределение
puasonDistribution() #распределение Пуасона
logDistribution() #логарифмическое распределение