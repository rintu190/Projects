import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
G = 6.6743e-11  # Gravitational constant
c = 299792458  # Speed of light
H0 = 70  # Hubble constant
rho_crit = 3*(H0**2)/(8*np.pi*G)  # Critical density of the universe

# Simulation parameters
tmax = 14e9  # Maximum simulation time (in years)
dt = 1e7  # Time step size (in years)
a0 = 1e-15  # Initial scale factor of the universe
N = int(tmax/dt)  # Number of time steps

# Initialize the universe
a = np.zeros(N)
a[0] = a0

# Simulate the universe
for i in range(1, N):
    t = i*dt
    a[i] = a0*np.exp(H0*t)

# Plot the universe animation
fig, ax = plt.subplots()

x = np.linspace(0, 1, 1000)
y = np.sin(x*np.pi)
line, = ax.plot(x, y, 'b-', lw=2)

def animate(i):
    ax.set_xlim(0, 1/a[i])
    ax.set_ylim(-1, 1)
    line.set_xdata(np.linspace(0, 1/a[i], 1000))
    return line,

ani = animation.FuncAnimation(fig, animate, frames=N, interval=50, blit=True)
plt.show()