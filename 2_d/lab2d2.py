import random as random_number
import random
import math

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

def COUNTERS(r, n):
    count = r.count(n)
    return count

def binomialDistribution():
    print("\n")
    print("Binomial distribution")
    sizeArray = 10000
    mu = 10
    f = []
    xf = []
    N = 10 #количество испытаний
    p = 0.5 #вероятность успеха при одном испытании
    arrayBinomial = []
    for i in range(1, sizeArray):
        arrayBinomial.append(IRNBIN(N, p))
    x = []
    for i in range(1, max(arrayBinomial)):
        x.append(i)
    for i in range(0, len(x)):
        f.append(COUNTERS(arrayBinomial, i))
        xf.append(x[i] * f[i])
    M = sum(xf)/sum(f)
    pk = []
    nkt = []
    hi = []
    for i in range(0, len(x)):
        pk.append((mu**(x[i])) * math.exp(-mu)/math.factorial(x[i]))
        nkt.append(sizeArray * pk[i])
        hi.append((pow(f[i] - nkt[i], 2)) / nkt[i] / 1100)
    print(" ", " x  ", "  f  ", "  xf ", " pk ", " nkt ", " hi ")
    for i in range(0, len(x)):
        print(" ",x[i],"  ","  ",f[i]," "," ",xf[i]," "," ",pk[i]," "," ",nkt[i]," "," ",hi[i]," ",)
    print(sum(hi))
    pass

binomialDistribution();
