import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.6743e-11  # Gravitational constant
c = 299792458  # Speed of light
M = 10  # Mass of the black hole (in solar masses)
Rs = 2*G*M/(c**2)  # Schwarzschild radius of the black hole

# Simulation parameters
N = 1000  # Number of points in the grid
xmin, xmax, ymin, ymax = -5*Rs, 5*Rs, -5*Rs, 5*Rs  # Limits of the plot

# Create the grid
x = np.linspace(xmin, xmax, N)
y = np.linspace(ymin, ymax, N)
xx, yy = np.meshgrid(x, y)
r = np.sqrt(xx**2 + yy**2)
theta = np.arctan2(yy, xx)

# Calculate the Schwarzschild metric
g_tt = -(1 - Rs/r)
g_rr = 1/(1 - Rs/r)
g_theta_theta = r**2
g_phi_phi = r**2 * np.sin(theta)**2
g = np.array([g_tt, g_rr, g_theta_theta, g_phi_phi]).T.reshape(-1, 4)

# Calculate the geodesic equation
v = np.array([[1, 0, 0, 0]] * N)  # Initial 4-velocity
t = np.zeros(N)
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
phi = np.zeros(N)

for i in range(1, N):
    dt = 0.01  # Time step size
    dr = v[i, 1]*dt
    dtheta = v[i, 2]*dt
    dphi = v[i, 3]*dt

    a = -G*M/r[i]**2 * g[i] @ v[i]
    v[i] += a*dt

    t[i] = t[i-1] + dt
    x[i] = x[i-1] + dr*np.sin(theta[i])*np.cos(phi[i])
    y[i] = y[i-1] + dr*np.sin(theta[i])*np.sin(phi[i])
    z[i] = z[i-1] + dr*np.cos(theta[i])
    phi[i] = phi[i-1] + dphi

# Plot the black hole
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.contour(xx, yy, r, [Rs], colors='black')
ax.plot(x, y, 'r-', lw=2)
plt.show()