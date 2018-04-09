import random
import numpy as np
import matplotlib.pyplot as plt

def RNSTUD(N):
    z = np.random.normal(0, 1)
    Yn = RNCHIS(N)
    t = z/np.sqrt(Yn/N)
    return t

def studentDist():
    arrayStud = []
    sizeArray = 10000
    for i in range(1, sizeArray):
        arrayStud.append(RNSTUD(10))
    from numpy import mean, var
    print("RNSTUD:")
    m = mean(arrayStud)  # мат. одидание
    print("mean = ", m)
    v = var(arrayStud)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayStud) / float(len(arrayStud))
    amounts, bins, _ = plt.hist(arrayStud, weights=weights)
    plt.savefig('denstFunctStud.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctStud.png')
    pass

def RNCHIS(N):
    u = np.random.normal(0, 1, N)
    r = sum(u**2)
    return r

def hi_squareDist():
    arrayHi = []
    sizeArray = 10000
    for i in range(1, sizeArray):
        arrayHi.append(RNCHIS(10))
    from numpy import mean, var
    print("RNCHIS:")
    m = mean(arrayHi)  # мат. одидание
    print("mean = ", m)
    v = var(arrayHi)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayHi) / float(len(arrayHi))
    amounts, bins, _ = plt.hist(arrayHi, weights=weights)
    plt.savefig('denstFunctHi.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctHi.png')
    pass

def RNEXP(b):
    u = random.random()
    r = -b * np.log(u)
    return r

def exponentDist():
    arrayExp = []
    sizeArray = 10000
    for i in range(1, sizeArray):
        arrayExp.append(RNEXP(1))
    from numpy import mean, var
    print("RNEXP:")
    m = mean(arrayExp)  # мат. одидание
    print("mean = ", m)
    v = var(arrayExp)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayExp) / float(len(arrayExp))
    amounts, bins, _ = plt.hist(arrayExp, weights=weights)
    plt.savefig('denstFunctExp.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctExp.png')
    pass

def RNRM_1():
    u1 = random.random()
    u2 = random.random()
    z = np.sqrt(-2 * np.log(u2)) * np.cos(2 * np.pi * u1)
    return z


def RNRM_2():
    u = []
    for i in range(0, 12):
        u.append(random.random())
    r = sum(u) - 6
    return r


def normalDist():
    arrayNorm = []
    sizeArray = 10000
    for i in range(1, sizeArray):
        arrayNorm.append(RNRM_1())
    from numpy import mean, var
    print("RNRM_1:")
    m = mean(arrayNorm)  # мат. одидание
    print("mean = ", m)
    v = var(arrayNorm)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayNorm) / float(len(arrayNorm))
    amounts, bins, _ = plt.hist(arrayNorm, weights=weights)
    plt.savefig('denstFunctNorm_RNRM_1.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctNorm_RNRM_1.png')
    arrayNorm.clear()
    for i in range(1, sizeArray):
        arrayNorm.append(RNRM_2())
    from numpy import mean, var
    print("RNRM_2:")
    m = mean(arrayNorm)  # мат. одидание
    print("mean = ", m)
    v = var(arrayNorm)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayNorm) / float(len(arrayNorm))
    amounts, bins, _ = plt.hist(arrayNorm, weights=weights)
    plt.savefig('denstFunctNorm_RNRM_2.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctNorm_RNRM_2.png')
    pass


def RNUNI(a, b):
    u = random.random()
    r = (b - a) * u + a
    return r


def uniformDist():
    arrayUnif = []
    sizeArray = 10000
    for i in range(1, sizeArray):
        arrayUnif.append(RNUNI(1, 5))
    from numpy import mean, var
    print("RNUNI:")
    m = mean(arrayUnif)  # мат. одидание
    print("mean = ", m)
    v = var(arrayUnif)  # дисперсия
    print("var = ", v)
    plt.figure()
    plt.title(f'Density function, n = {sizeArray}')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    weights = np.ones_like(arrayUnif) / float(len(arrayUnif))
    amounts, bins, _ = plt.hist(arrayUnif, weights=weights)
    plt.savefig('denstFunctUnif.png')
    plt.figure()
    plt.ylabel('F(x)')
    plt.xlabel('x')
    plt.title(f'Integrate function, n = {sizeArray}')
    plt.plot(bins, distribution(amounts, bins))
    plt.savefig('integFunctUnif.png')
    pass


def distribution(amounts, bins):
    amounts = np.insert(amounts, 0, 0.)
    n = sum(amounts)
    return [sum(amounts[:i + 1]) / n for i, bin in enumerate(bins)]


uniformDist()
normalDist()
exponentDist()
hi_squareDist()
studentDist()
