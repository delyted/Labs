import numpy as np
import matplotlib.pyplot as plt

nx = 100 
nt = 20 
L = 100.0 
dx = L / nx
dt = 0.001 
Vmax = 90.0 
rho_max = 15.0 


rho = np.ones(nx)*rho_max/2
v = np.zeros(nx)


for n in range(nt):

    q = rho*v
    
    q[0] = q[nx-1]
    
    rho_gradient = np.diff(rho)/dx

    v = Vmax*(1 - rho/rho_max)

    delta_rho = -dt*np.diff(q)/dx
    
    delta_rho = np.append(delta_rho, delta_rho[0])
    
    rho += delta_rho
    
    rho = np.maximum(0, np.minimum(rho, rho_max))
    
    if n % 10 == 0:
        plt.clf()
        plt.plot(np.linspace(0, L, nx), rho)
        plt.plot(np.linspace(0, L, nx), v)
        plt.xlabel('Position')
        plt.ylabel('Density / Velocity')
        plt.ylim([0, Vmax*1.2])
        plt.pause(0.001)

plt.show()