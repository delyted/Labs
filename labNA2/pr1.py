import numpy as np
def Legendre(n, x):
    x = np.array(x)
    if n == 0:
        return x * 0 + 1.0
    elif n == 1:
        return x
    else:
        return ((2.0 * n - 1.0) * x * Legendre(n - 1, x) - (n - 1) * Legendre(n - 2, x)) / n

def DLegendre(n, x):
    x = np.array(x)
    if n == 0:
        return x * 0
    elif n == 1:
        return x * 0 + 1.0
    else:
        return (n / (x ** 2 - 1.0)) * (x * Legendre(n, x) - Legendre(n - 1, x))

def LegendreRoots(polyorder, tolerance=1e-20):
    global roots
    if polyorder < 2:
        err = 1  
    else:
        roots = []

        for i in range(1, int(polyorder) // 2 + 1):
            x = np.cos(np.pi * (i - 0.25) / (polyorder + 0.5))
            error = 10 * tolerance
            iters = 0
            while (error > tolerance) and (iters < 1000):
                dx = -Legendre(polyorder, x) / DLegendre(polyorder, x)
                x = x + dx
                iters = iters + 1
                error = abs(dx)
            roots.append(x)

        roots = np.array(roots)
        if polyorder % 2 == 0:
            roots = np.concatenate((-1.0 * roots, roots[::-1]))
        else:
            roots = np.concatenate((-1.0 * roots, [0.0], roots[::-1]))
        err = 0 
    return [roots, err]


def GaussLegendreWeights(polyorder):
    W = []
    [xis, err] = LegendreRoots(polyorder)
    if err == 0:
        W = 2.0 / ((1.0 - xis ** 2) * (DLegendre(polyorder, xis) ** 2))
        err = 0
    else:
        err = 1 
    return [W, xis, err]

def GaussLegendreQuadrature(func, polyorder, a, b):
    [Ws, xs, err] = GaussLegendreWeights(polyorder)
    if err == 0:
        ans = (b - a) * 0.5 * sum(Ws * func((b - a) * 0.5 * xs + (b + a) * 0.5))
    else:
        
        err = 1
        ans = None
    return [ans, err]


def func(x):
    return np.cos(x**2)+ np.sin(x)

print("enter your order:  ")
order = int(input())
[Ws, xs, err] = GaussLegendreWeights(order)
if err == 0:
    print("Number of points  : ", order)
    print("Weights  : ", Ws)    
    print("Roots    : ", xs)     

else:
    print("Roots/Weights evaluation failed")


[ans, err] = GaussLegendreQuadrature(func, order, -2, 2)
if err == 0:
    print("Integral: ", ans)
else:
    print("Integral evaluation failed")