import numpy as np
import sympy

equations = []

print("Input your equations: ")
while True:
    equation = input().replace("−", "-")
    if equation != "end":
        equations.append(equation)
    else:
        break

symbols = [sympy.symbols("x" + str(i + 1)) for i in range(len(equations))]

print("\nGive your initial guesses!")
x0 = np.array([[float(input(f"x{i+1}="))] for i in range(len(equations))])

tolerance = float(input("tolerance:"))

simplified_equations = []
for equation in equations:
    for symbol in symbols:
        c = equation.find(str(symbol))
        if equation[c] != "0" and c != 0 and equation[c-1].isdigit():
            equation = equation[:c] + "*" + equation[c:]
    equation = equation.split("=")
    simplified_equations.append(sympy.simplify(equation[0]) - sympy.simplify(equation[1]))

error = 1
while error > tolerance:
    dic = {}
    for i in range(len(x0)):
        dic[symbols[i]] = x0[i][0]
    jacobian = []
    for equation in simplified_equations:
        row = []
        for symbol in symbols:
            row.append(float(equation.diff(symbol).subs(dic).evalf()))
        jacobian.append(row)
    jacobian = np.array(jacobian)

    values = np.array([[float(equation.subs(dic).evalf())] for equation in simplified_equations])

    delta_x = np.linalg.solve(jacobian, -values)

    xn1 = x0 + delta_x
    x0 = xn1

    error1 = sum(delta_x[i][0] ** 2 for i in range(len(delta_x)))
    error2 = sum(xn1[i][0] ** 2 for i in range(len(xn1)))
    error = error1 / error2

for i in range(len(symbols)):
    print(f"{symbols[i]} = {xn1[i][0]}")

print("error:", error)
