import math

def muller_method(f, x0, x1, x2, epsilon=1e-8, max_iterations=100):
    """Solves equation f(x) = 0 using Muller's method.

    Args:
        f (function): The function f(x) whose root needs to be found.
        x0 (float): Initial guess for the root.
        x1 (float): Initial guess for the root.
        x2 (float): Initial guess for the root.
        epsilon (float): Desired accuracy (default: 1e-8).
        max_iterations (int): Maximum number of iterations (default: 100).

    Returns:
        float: The root of the equation f(x) = 0.
    """
    h1 = x1 - x0
    h2 = x2 - x1
    delta1 = (f(x1) - f(x0)) / h1
    delta2 = (f(x2) - f(x1)) / h2
    d = (delta2 - delta1) / (h2 + h1)
    i = 3
    while i <= max_iterations:
        b = delta2 + h2 * d
        D = math.sqrt(b**2 - 4 * f(x2) * d)
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        h = -2 * f(x2) / E
        p = x2 + h
        if abs(h) < epsilon:
            return p
        x0 = x1
        x1 = x2
        x2 = p
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f(x1) - f(x0)) / h1
        delta2 = (f(x2) - f(x1)) / h2
        d = (delta2 - delta1) / (h2 + h1)
        i += 1
    raise ValueError("Muller's method failed to converge within the maximum number of iterations.")


# Define the equation x^3 + 2x^2 + 10x - 20 = 0
def equation(x):
    return x**3 + 2*x**2 + 10*x - 20


# Solve the equation using Muller's method
root = muller_method(equation, 0, 1, 2)
print(f"The Root is: {root:.8f}")
