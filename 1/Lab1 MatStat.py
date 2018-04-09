from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


def createList(n):
    numbers = np.random.uniform(0, 1, n)
    return numbers

def expecValue(n):
    M = sum(createList(n)) / n
    return M

def dispersion(list, M):
    sumPow = 0
    for i in range(0, n):
        sumPow += (list[i] - M) ** 2
    D = sumPow / n
    return D

def densityFunc(n, numbers):
    array = []
    for i in range(1, n):
        a = 0
        b = numbers[i]
        c = 1/(b-a)
        if numbers[i] >= a and numbers[i] <= b:
            array.append(c)
        else:
            array.append(0)
    return array

def autocorFunc(n, M, numbers):
    K = []
    for i in range(1, n):
        f = i
        sum1 = 0
        sum2 = 0
        for j in range(1, n - f):
            sum1 += (numbers[j] - M) * (numbers[j + f] - M)
        for g in range(1, n):
            sum2 += (numbers[g] - M) ** 2
        K.append(sum1/sum2)
    return K


n = 10
print("N = ", n)
numbers1 = createList(n)
M = expecValue(n)
D = dispersion(numbers1, M)
S = sqrt(D)
print("Numbers: \n", numbers1)
print("M: ", M)
print("D: ", D)
print("S: ", S)
K1 = autocorFunc(n, M, numbers1)
locs = np.arange(len(K1))
width = 0.75
plt.bar(locs, K1, width=width)
plt.ylabel('K(f)')
plt.xlabel('f')
plt.title('Correlogram, n=10')
plt.savefig('correl1.png')
plt.close()
densityFunc(n, numbers1)
weights = np.ones_like(numbers1) / float(len(numbers1))
plt.hist(numbers1, weights=weights)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.title('density function, n=10')
plt.savefig('denstFunct1.png')
numbers1.sort()
plt.close()
plt.plot(numbers1 / n)
plt.ylabel('F(x)')
plt.xlabel('x')
plt.title('integrate function, n=10')
plt.savefig("integFunct1.png")
plt.close()
print("\n")

n = 100
print("N = ", n)
numbers2 = createList(n)
M = expecValue(n)
D = dispersion(numbers2, M)
S = sqrt(D)
print("Numbers: \n", numbers2)
print("M: ", M)
print("D: ", D)
print("S: ", S)
K2 = autocorFunc(n, M, numbers2)
locs = np.arange(len(K2))
width = 0.75
plt.bar(locs, K2, width=width)
plt.ylabel('K(f)')
plt.xlabel('f')
plt.title('Correlogram, n=100')
plt.savefig('correl2.png')
plt.close()
densityFunc(n, numbers2)
weights = np.ones_like(numbers2) / float(len(numbers2))
plt.hist(numbers2, weights=weights)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.title('density function, n=100')
plt.savefig('denstFunct2.png')
numbers2.sort()
plt.close()
plt.plot(numbers2 / n)
plt.ylabel('F(x)')
plt.xlabel('x')
plt.title('integrate function, n=100')
plt.savefig("integFunct2.png")
plt.close()
print("\n")

n = 1000
print("N = ", n)
numbers3 = createList(n)
M = expecValue(n)
D = dispersion(numbers3, M)
S = sqrt(D)
print("Numbers: \n", numbers3)
print("M: ", M)
print("D: ", D)
print("S: ", S)
K3 = autocorFunc(n, M, numbers3)
locs = np.arange(len(K3))
width = 0.75
plt.bar(locs, K3, width=width)
plt.ylabel('K(f)')
plt.xlabel('f')
plt.title('Correlogram, n=1000')
plt.savefig('correl3.png')
plt.close()
densityFunc(n, numbers3)
weights = np.ones_like(numbers3) / float(len(numbers3))
plt.hist(numbers3, weights=weights)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.title('density function, n=1000')
plt.savefig('denstFunct3.png')
numbers3.sort()
plt.close()
plt.plot(numbers3 / n)
plt.ylabel('F(x)')
plt.xlabel('x')
plt.title('integrate function, n=1000')
plt.savefig("integFunct3.png")
plt.close()
print("\n")

n = 10000
K4 = []
print("N = ", n)
numbers4 = createList(n)
M = expecValue(n)
D = dispersion(numbers4, M)
S = sqrt(D)
print("Numbers: \n", numbers4)
print("M: ", M)
print("D: ", D)
print("S: ", S)
K4 = autocorFunc(n, M, numbers4)
locs = np.arange(len(K4))
width = 0.75

plt.bar(locs, K4, width=width)
plt.ylabel('K(f)')
plt.xlabel('f')
plt.title('Correlogram, n=10000')
plt.savefig('correl4.png')
plt.close()
densityFunc(n, numbers4)
weights = np.ones_like(numbers4) / float(len(numbers4))
plt.hist(numbers4, weights=weights)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.title('density function, n=10000')
plt.savefig('denstFunct4.png')
numbers4.sort()
plt.close()
plt.plot(numbers4 / n)
plt.ylabel('F(x)')
plt.xlabel('x')
plt.title('integrate function, n=10000')
plt.savefig("integFunct4.png")
plt.close()
print("\n")