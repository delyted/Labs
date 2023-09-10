import numpy as np
from scipy.interpolate import lagrange, interp1d, BarycentricInterpolator, CubicSpline
from scipy.integrate import romberg

data = np.loadtxt('D:\Codes\python\labNA2\dataset_3.txt', delimiter=',', skiprows=1)
x = data[:, 0]
y = data[:, 1]

lagrange_interp = lagrange(x, y)
linear_interp = interp1d(x, y, kind='linear')
newton_interp = BarycentricInterpolator(x, y).__call__(x)
cubic_spline_interp = CubicSpline(x, y)

def f(x):
    return cubic_spline_interp(x)

a = x[0]
b = x[-1]
n = 5

area = romberg(f, a, b, divmax=20, show=False)

print(f"Lagrange Interpolation at x=5: {lagrange_interp(5)}")
print(f"Linear Interpolation at x=5: {linear_interp(5)}")
print(f"Newton Interpolation at x=5: {newton_interp[4]}")
print(f"Cubic Spline Interpolation at x=5: {cubic_spline_interp(5)}")
print(f"Area under the curve using Romberg integration: {area}")