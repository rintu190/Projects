import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric_posvel

# Define the bodies we want to simulate
bodies = ['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

# Define the initial time and time step
t0 = Time('2023-01-01 00:00:00', scale='utc')
t1 = Time('2024-01-01 00:00:00', scale='utc')
dt = 1 * u.day

# Set the solar system ephemeris
solar_system_ephemeris.set('de432s')

# Initialize arrays to store the positions of the bodies
positions = {}

# Loop over time steps
for t in np.arange(t0, t1, dt):
    # Get the positions of each body at the current time step
    for body in bodies:
        pos, vel = get_body_barycentric_posvel(body, t)
        positions.setdefault(body, []).append(pos.to(u.au).value)

# Plot the positions of the bodies over time
fig, ax = plt.subplots()
for body in bodies:
    pos = np.array(positions[body])
    ax.plot(pos[:, 0], pos[:, 1], label=body)
ax.set_xlabel('x (AU)')
ax.set_ylabel('y (AU)')
ax.set_title('Simulating Our Solar System')
ax.legend()
plt.show()