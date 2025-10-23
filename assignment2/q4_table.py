import numpy as np

# Constants
RE = 6371  # Earth radius in km
H = 1000   # Satellite altitude in km
f = 2e9    # Frequency in Hz (2.0 GHz)
c = 3e8    # Speed of light in m/s
EIRP = 13  # EIRP in dBW (Tx power 10 dBW + antenna gain 3 dBi)

# Elevation angles from 0 to 90 degrees in 10 degree increments
el_deg = np.arange(0, 91, 10)
el_rad = np.deg2rad(el_deg)

# Calculate slant range d in km
d_km = RE * (np.sqrt((1 + H / RE)**2 - np.cos(el_rad)**2) - np.sin(el_rad))

# Convert slant range to meters
d_m = d_km * 1000

# Calculate free space loss Ls in dB
Ls = 20 * np.log10(4 * np.pi * d_m * f / c)

# Calculate received power Pr in dBW
Pr = EIRP - Ls

# Print the table
print("Elevation | Slant Range | Free Space Loss | Received Power")
print("(deg)     | (km)        | (dB)            | (dBW)         ")
print("-" * 55)
for i in range(len(el_deg)):
    print(f"{el_deg[i]:<10}| {d_km[i]:<11.1f} | {Ls[i]:<15.1f} | {Pr[i]:<13.1f}")