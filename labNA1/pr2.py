def g(x, c):
    return 2*x - c*x**2

def dg(x, c):
    return 2 - 2*c*x

def fixed_point_iteration(c, p0, eps=1e-8, max_iter=1000):
    p = p0
    for i in range(max_iter):
        p_prev = p
        p = g(p_prev, c)
        if abs(p - p_prev) < eps:
            return p
    return None

c = 2  # positive constant
p0 = 0.5 # initial guess
p_star = fixed_point_iteration(c, p0)
if p_star is not None:
    print(f"The limit of the fixed-point iteration is {p_star:.8f}, which is equal to 1/c = {1/c:.8f}.")
else:
    print("The fixed-point iteration did not converge to a non-zero limit.")