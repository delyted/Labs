import numpy as np
from scipy.interpolate import Rbf

data = np.loadtxt('D:\Codes\python\labNA2\map.txt', delimiter='\t', skiprows=1, usecols=(0, 1))

known_points = data[~np.isnan(data[:, 1])]
unknown_points = data[np.isnan(data[:, 1])]

rbf = Rbf(known_points[:, 0], known_points[:, 1], function='linear')
unknown_values = rbf(unknown_points[:, 0], unknown_points[:, 1])

data[np.isnan(data[:, 1]), 1] = unknown_values

x, y = np.meshgrid(np.arange(6), np.arange(3))
A = np.vstack((x.flatten(), y.flatten(), np.ones(x.size))).T
b = data[:, 1].reshape(-1, 1)

coeffs = np.linalg.solve(A, b)
safest_path = coeffs[:2] @ np.array([[0, 1, 2, 3, 4, 5], [0, 0, 0, 0, 0, 0]])

print("The safest path to reach the lost city is:", safest_path)