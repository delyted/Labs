import math

def hybrid_secant_bisection(equation_func, lower_bound, upper_bound, tolerance, max_iterations):
    iterations = 0
    x0 = lower_bound
    x1 = upper_bound

    while iterations < max_iterations:
        f0 = equation_func(x0)
        f1 = equation_func(x1)
        f_diff = f1 - f0
        x_diff = x1 - x0

        if f_diff == 0:
            return x1

        df_dx1 = f_diff / x_diff
        x_next = x1 - f1 / df_dx1

        if x_next < lower_bound or x_next > upper_bound:
            x_next = (lower_bound + upper_bound) / 2

        if abs(equation_func(x_next)) < tolerance:
            return x_next

        x0 = x1
        x1 = x_next
        iterations += 1

    return x1

def equation_func(x):
    return eval(user_equation)

user_equation = input("Enter equation: ")
lower_bound = float(input("Enter the value of the lower bound: "))
upper_bound = float(input("Enter the value of the upper bound: "))

root = hybrid_secant_bisection(equation_func, lower_bound, upper_bound, 1e-6, 1000)

print("Root found:", root)
#x**3 + 2*x**2 - 7