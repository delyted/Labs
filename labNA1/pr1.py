import math

def bisection(f, a, b, tol=1e-8):
    if f(a) * f(b) >= 0:
        raise ValueError("Function must have opposite signs at endpoints")
    
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

def func(x):
    return math.exp(x) - x ** 2

a, b = -2, 0
root = bisection(func, a, b)

print(f"Root of the equation e^x - x^2 = 0 on the interval [-2, 0] is: {root:.8f}")
