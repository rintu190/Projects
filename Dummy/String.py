import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1.0  # Length of the string
T = 1.0  # Tension of the string
mu = 0.01  # Mass per unit length of the string

# Simulation parameters
dx = 0.01  # Spatial step size
dt = 0.001  # Time step size
tmax = 1.0  # Maximum simulation time

# Derived parameters
c = np.sqrt(T/mu)  # Wave speed
N = int(L/dx)  # Number of spatial points
M = int(tmax/dt)  # Number of time steps

# Initialize the string
x = np.linspace(0, L, N)
y = np.sin(np.pi*x/L)
y_prev = y.copy()

# Simulate the string
for i in range(1, M+1):
    # Apply the wave equation
    y_next = 2*y - y_prev + (c*dt/dx)**2 * (np.roll(y, 1) - 2*y + np.roll(y, -1))
    
    # Apply boundary conditions
    y_next[0] = y_next[-1] = 0
    
    # Update the string
    y_prev = y.copy()
    y = y_next.copy()
    
    # Plot the string
    if i % 10 == 0:  # Plot every 10 time steps
        plt.clf()
        plt.plot(x, y, 'b-', lw=2)
        plt.xlim(0, L)
        plt.ylim(-1, 1)
        plt.title('Vibrating String Simulation')
        plt.xlabel('Position')
        plt.ylabel('Amplitude')
        plt.pause(0.001)

plt.show()