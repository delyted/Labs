import numpy as np


# Load matrix data from file
with open('D:\Codes\python\labNA3\matrix.txt', 'r') as file:
    matrix = [line.strip().split() for line in file]

# Extract names and numbers from the matrix data
names = [name.strip(" '[],") for name in matrix[0][1:] if len(name) > 3]
numbers = np.array([
    [float(x.replace(',', '').replace('[','').replace(']','')) for x in row[1:]]
    for row in matrix[1:]
])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(numbers)

# Find the index of the influential eigenvalue
influential_index = np.argmax(np.abs(eigenvalues))

# Retrieve the influential eigenvalue and its corresponding eigenvector
influential_eigenvalue = eigenvalues[influential_index]
influential_eigenvector = eigenvectors[:, influential_index]

# Print the influential eigenvalue and its corresponding eigenvector
print("The most influential person is ",names[influential_index],", with the Eigenvalue =",influential_eigenvalue)
print(" and corresponding Eigenvector:")
print(influential_eigenvector)
print()

# Print all eigenvalues and eigenvectors
for i, (eigval, eigvec) in enumerate(zip(eigenvalues, eigenvectors.T), start=1):
    print("\n")
    print(f"Eigenvalue lambda{i}:" ,eigval)
    print(f"Eigenvector v{i}:")
    print(eigvec)
    print()

# Sort eigenvalues and eigenvectors in descending order based on eigenvalues
sort_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sort_indices]
eigenvectors = eigenvectors[:, sort_indices]

# Print the sorted eigenvalues
print("\n")
print("Sorted eigenvalues:")
for eigenvalue in eigenvalues:
    print(eigenvalue)
print()

# Print the sorted eigenvectors
print("Sorted eigenvectors:")
for eigenvector in eigenvectors.T:
    print(eigenvector)