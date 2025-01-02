import numpy as np
import matplotlib.pyplot as plt

# Define the magnetic field and area functions
def B(x):
    return np.array([0, 0, 0.1*np.sin(2*np.pi*x)])

def A(x):
    return np.array([0, 0.1*np.cos(2*np.pi*x), 0])

# Define the length of the wire and the number of time steps
L = 1
Nt = 100
dt = 0.01

# Initialize arrays to store the results
t = np.linspace(0, dt*Nt, Nt)
E = np.zeros(Nt)

# Loop over time steps
for i in range(Nt):
    x = L*(i/Nt)  # Calculate the position of the wire
    dBdt = (B(x+dt)-B(x))/dt  # Calculate the rate of change of the magnetic field
    E[i] = -np.dot(A(x), dBdt)  # Calculate the induced emf using Faraday's law

# Plot the results
fig, ax = plt.subplots()
ax.plot(t, E)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Induced emf (V)')
ax.set_title('Faraday\'s Law of Electromagnetic Induction')
plt.show()