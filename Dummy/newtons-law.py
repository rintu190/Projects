import matplotlib.pyplot as plt
import numpy as np

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
m = 0.1  # Mass of the ball (kg)

# Initial conditions
v0 = 10  # Initial velocity (m/s)
y0 = 0  # Initial height (m)
t0 = 0  # Initial time (s)

# Simulation parameters
dt = 0.01  # Time step size
tmax = 2*v0/g  # Total simulation time

# Initialize arrays to store the results
t = np.arange(t0, tmax, dt)
y = np.zeros_like(t)
v = np.zeros_like(t)
a = np.zeros_like(t)

# Set initial conditions
y[0] = y0
v[0] = v0
a[0] = -g

# Simulate the motion of the ball using Euler's method
for i in range(1, len(t)):
    a[i] = -g  # Calculate acceleration at this time step
    v[i] = v[i-1] + a[i]*dt  # Calculate velocity at this time step
    y[i] = y[i-1] + v[i]*dt  # Calculate height at this time step

# Plot the results
fig, ax = plt.subplots()
ax.plot(t, y)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Height (m)')
ax.set_title('Motion of a Ball Thrown Upwards')
plt.show()