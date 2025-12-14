import matplotlib.pyplot as plt
import numpy as np

# Constants (from Ch4)
Re = 6371  # Earth radius km
H = 800    # Satellite altitude km
r = Re + H  # Orbital radius

# Angles for diagram (in degrees)
el = 0  # Elevation angle for horizon

# Plot Earth as circle
theta = np.linspace(0, 2*np.pi, 100)
x_earth = Re * np.cos(theta)
y_earth = Re * np.sin(theta)
plt.plot(x_earth, y_earth, 'b', label='Earth')

# Ground station P at bottom (simplified)
plt.plot(0, 0, 'ro', label='Ground Station (P)')

# Satellite SAT position for example (at horizon for ideal)
# Calculate position: at el=0, d_max = sqrt(H*(2*Re + H))
d_max = np.sqrt(H * (2 * Re + H))
sat_x = d_max  # Place to right for side view
sat_y = 0      # At horizon level
plt.plot(sat_x, sat_y, 'go', label='Satellite (SAT)')

# Horizon plane as tangent line at P (horizontal base)
plt.axhline(y=0, color='k', linestyle='--', label='Ideal Horizon Plane (Tangent at P)')

# Slant range d (line P to SAT)
plt.plot([0, sat_x], [0, sat_y], 'g--', label='Slant Range (d)')

# Labels
plt.text(0, -Re/10, 'Earth Center (O)', horizontalalignment='center')
plt.text(sat_x / 2, sat_y / 2 + Re/10, 'Elevation El=0° (Horizon)', color='g')
plt.text(Re / 2, Re / 2, f'H = {H} km', color='b')

# Setup plot
plt.axis('equal')
plt.xlim(-Re/2, Re + d_max)
plt.ylim(-Re/2, Re/2)
plt.xlabel('Distance (km)')
plt.ylabel('Height (km)')
plt.title('Side-View Geometry of Ideal Horizon Plane for LEO Satellite')
plt.legend()
plt.grid(True)
plt.show()