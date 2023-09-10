import numpy as np

# Define the coefficients of the linear equations as a list of arrays
A = [np.array([[2, -1]]), np.array([[3, 2]]), np.array([[1, 1]]), np.array([[4, -1]]), np.array([[1, -3]])]

# Define the constants of the linear equations as a list
b = [4, 7, 3, 1, -2]

# Solve each equation separately and store the solutions
solutions = [np.linalg.lstsq(coef, [const], rcond=None)[0] for coef, const in zip(A, b)]

# Convert the solutions list to a numpy array
solutions = np.array(solutions)

# Determine the correct order in which to step on the stones based on the solutions
order = np.lexsort(solutions.T)

# Print the correct order in which to step on the stones
print("Correct order:", order + 1)