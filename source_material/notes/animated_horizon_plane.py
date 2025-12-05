"""
Animated visualization of LEO satellite pass showing:
- Satellite motion along orbit
- Elevation angle changes
- Ideal vs. Designed horizon planes
- Slant range variation
- Key geometric angles (nadir, central, elevation)
- AOS/LOS markers

Based on Chapter 4 concepts from Ground Station Design textbook
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Arc, FancyArrowPatch
import numpy as np

# Constants (from Chapter 4)
R_E = 6371  # Earth radius km
H = 1000    # Satellite altitude km (from Assignment 2)
r = R_E + H  # Orbital radius

# Designed elevation angle
DESIGNED_EL = 30  # degrees

# Ground station location (on Earth's surface)
# Place at angle theta_gs from vertical for better visualization
theta_gs = 0  # degrees (at equator, facing right)
gs_x = R_E * np.cos(np.radians(theta_gs))
gs_y = R_E * np.sin(np.radians(theta_gs))

# Calculate key angles for ideal horizon (el = 0°)
alpha_0_max = np.degrees(np.arcsin(R_E / r))  # Max nadir angle
gamma_max = 2 * alpha_0_max  # Central angle for full visibility

# Calculate angles for designed horizon (el = 30°)
sin_alpha_30 = (R_E / r) * np.cos(np.radians(DESIGNED_EL))
alpha_30 = np.degrees(np.arcsin(sin_alpha_30))
beta_30 = 90 - DESIGNED_EL - alpha_30
gamma_30 = 2 * beta_30  # Central angle for designed visibility

# Satellite orbital positions (centered at Earth center)
# Pass overhead from -gamma_max/2 to +gamma_max/2
num_frames = 150
theta_sat_array = np.linspace(-gamma_max/2 - 20, gamma_max/2 + 20, num_frames)

# Calculate slant range as function of elevation angle
def slant_range(elevation_deg):
    """Calculate slant range from ground station to satellite"""
    el_rad = np.radians(elevation_deg)
    d = R_E * (np.sqrt((1 + H/R_E)**2 - np.cos(el_rad)**2) - np.sin(el_rad))
    return d

def calculate_elevation(sat_x, sat_y, gs_x, gs_y):
    """Calculate elevation angle from ground station to satellite"""
    # Vector from ground station to satellite
    dx = sat_x - gs_x
    dy = sat_y - gs_y

    # Vector from Earth center to ground station (outward normal)
    gsx_norm = gs_x
    gsy_norm = gs_y

    # Angle between horizon plane (perpendicular to normal) and slant range
    # Elevation = 90° - angle between normal and slant range
    dot_product = dx * gsx_norm + dy * gsy_norm
    mag_gs = np.sqrt(gsx_norm**2 + gsy_norm**2)
    mag_slant = np.sqrt(dx**2 + dy**2)

    if mag_gs == 0 or mag_slant == 0:
        return 0

    cos_angle = dot_product / (mag_gs * mag_slant)
    cos_angle = np.clip(cos_angle, -1, 1)
    angle_from_normal = np.degrees(np.arccos(cos_angle))

    elevation = angle_from_normal - 90
    return elevation

# Setup figure - much larger with proper spacing to fit all content
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 11))
fig.subplots_adjust(left=0.06, right=0.98, top=0.93, bottom=0.07, wspace=0.25)
fig.suptitle('LEO Satellite Pass: Elevation Angles and Horizon Planes\n(Chapter 4 Concepts)',
             fontsize=16, fontweight='bold')

# Initialize plot elements
def init():
    ax1.clear()
    ax2.clear()
    return []

def animate(frame):
    ax1.clear()
    ax2.clear()

    # Current satellite position
    theta_sat = theta_sat_array[frame]
    sat_x = r * np.cos(np.radians(theta_sat))
    sat_y = r * np.sin(np.radians(theta_sat))

    # Calculate current elevation angle
    current_elevation = calculate_elevation(sat_x, sat_y, gs_x, gs_y)

    # Calculate slant range
    d = np.sqrt((sat_x - gs_x)**2 + (sat_y - gs_y)**2)

    # === LEFT PLOT: Geometric View ===
    ax1.set_aspect('equal')
    ax1.set_xlim(-R_E*1.2, r*1.2)
    ax1.set_ylim(-r*1.2, r*1.2)  # Much taller to show full orbit
    ax1.set_xlabel('Distance (km)', fontsize=10)
    ax1.set_ylabel('Height (km)', fontsize=10)
    ax1.set_title('Side View: Satellite Geometry', fontsize=12)
    ax1.grid(True, alpha=0.3)

    # Draw Earth
    theta_earth = np.linspace(0, 2*np.pi, 100)
    x_earth = R_E * np.cos(theta_earth)
    y_earth = R_E * np.sin(theta_earth)
    ax1.fill(x_earth, y_earth, color='lightblue', alpha=0.5, label='Earth')
    ax1.plot(x_earth, y_earth, 'b-', linewidth=2)

    # Draw satellite orbit
    theta_orbit = np.linspace(0, 2*np.pi, 100)
    x_orbit = r * np.cos(theta_orbit)
    y_orbit = r * np.sin(theta_orbit)
    ax1.plot(x_orbit, y_orbit, 'gray', linestyle='--', linewidth=1, alpha=0.3, label='Orbit')

    # Draw visible arc (ideal horizon - 0° elevation)
    theta_visible = np.linspace(np.radians(-gamma_max/2), np.radians(gamma_max/2), 50)
    x_visible = r * np.cos(theta_visible)
    y_visible = r * np.sin(theta_visible)
    ax1.plot(x_visible, y_visible, 'g-', linewidth=3, alpha=0.7, label=f'Visible Arc (0°)')

    # Draw designed horizon arc (30° elevation)
    theta_designed = np.linspace(np.radians(-gamma_30/2), np.radians(gamma_30/2), 50)
    x_designed = r * np.cos(theta_designed)
    y_designed = r * np.sin(theta_designed)
    ax1.plot(x_designed, y_designed, 'orange', linewidth=3, alpha=0.7, label=f'Locked Arc ({DESIGNED_EL}°)')

    # Mark AOS/LOS for ideal horizon
    aos_x = r * np.cos(np.radians(-gamma_max/2))
    aos_y = r * np.sin(np.radians(-gamma_max/2))
    los_x = r * np.cos(np.radians(gamma_max/2))
    los_y = r * np.sin(np.radians(gamma_max/2))
    ax1.plot(aos_x, aos_y, 'go', markersize=8, label='AOS (0°)')
    ax1.plot(los_x, los_y, 'ro', markersize=8, label='LOS (0°)')

    # Mark AOS/LOS for designed horizon
    aos_30_x = r * np.cos(np.radians(-gamma_30/2))
    aos_30_y = r * np.sin(np.radians(-gamma_30/2))
    los_30_x = r * np.cos(np.radians(gamma_30/2))
    los_30_y = r * np.sin(np.radians(gamma_30/2))
    ax1.plot(aos_30_x, aos_30_y, 'o', color='orange', markersize=8)
    ax1.plot(los_30_x, los_30_y, 'o', color='orange', markersize=8)

    # Ground station
    ax1.plot(gs_x, gs_y, 'k^', markersize=15, label='Ground Station', zorder=10)

    # Current satellite position
    ax1.plot(sat_x, sat_y, 'r*', markersize=20, label='Satellite', zorder=10)

    # Slant range line
    ax1.plot([gs_x, sat_x], [gs_y, sat_y], 'r--', linewidth=2, alpha=0.7, label=f'Slant Range: {d:.0f} km')

    # Ideal horizon plane (tangent at ground station)
    horizon_angle = np.radians(theta_gs + 90)
    horizon_length = R_E * 1.5
    horizon_x1 = gs_x - horizon_length * np.cos(horizon_angle)
    horizon_y1 = gs_y - horizon_length * np.sin(horizon_angle)
    horizon_x2 = gs_x + horizon_length * np.cos(horizon_angle)
    horizon_y2 = gs_y + horizon_length * np.sin(horizon_angle)
    ax1.plot([horizon_x1, horizon_x2], [horizon_y1, horizon_y2], 'g--',
             linewidth=2, alpha=0.5, label='Ideal Horizon (0°)')

    # Designed horizon plane (parallel to ideal, at 30°)
    # Calculate LDHPW (Layer Distance between planes)
    sin_alpha_D = (R_E / r) * np.cos(np.radians(DESIGNED_EL))
    alpha_D = np.arcsin(sin_alpha_D)
    L_DHPW = H - R_E * (1 / np.cos(alpha_D) - 1)

    designed_offset = L_DHPW
    designed_x1 = horizon_x1 - designed_offset * np.sin(horizon_angle)
    designed_y1 = horizon_y1 + designed_offset * np.cos(horizon_angle)
    designed_x2 = horizon_x2 - designed_offset * np.sin(horizon_angle)
    designed_y2 = horizon_y2 + designed_offset * np.cos(horizon_angle)
    ax1.plot([designed_x1, designed_x2], [designed_y1, designed_y2],
             color='orange', linestyle='--', linewidth=2, alpha=0.5, label=f'Designed Horizon ({DESIGNED_EL}°)')

    # Line from Earth center to satellite (for nadir angle)
    ax1.plot([0, sat_x], [0, sat_y], 'purple', linestyle=':', linewidth=1, alpha=0.5)

    # Line from Earth center to ground station
    ax1.plot([0, gs_x], [0, gs_y], 'black', linestyle=':', linewidth=1, alpha=0.5)

    ax1.legend(loc='upper right', fontsize=8)

    # === RIGHT PLOT: Information Display ===
    ax2.axis('off')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # Display current parameters
    info_text = f"""
SATELLITE PARAMETERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Altitude (H):        {H} km
Orbital Radius (r):  {r} km
Earth Radius (R_E):  {R_E} km

CURRENT MEASUREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Elevation Angle:     {current_elevation:.1f}°
Slant Range (d):     {d:.0f} km
Satellite Position:  {theta_sat:.1f}°

IDEAL HORIZON (0° Elevation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Max Nadir Angle:     {alpha_0_max:.2f}°
Central Angle:       {gamma_max:.2f}°
Max Slant Range:     {slant_range(0):.0f} km

DESIGNED HORIZON ({DESIGNED_EL}° Elevation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nadir Angle (α₀):    {alpha_30:.2f}°
Central Angle (β₀):  {beta_30:.2f}°
Visibility Arc:      {gamma_30:.2f}°
Slant Range at {DESIGNED_EL}°:  {slant_range(DESIGNED_EL):.0f} km

COMMUNICATION STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    # Determine communication status
    if current_elevation < 0:
        status = "⚫ BELOW HORIZON - No Signal"
        status_color = 'red'
    elif current_elevation < DESIGNED_EL:
        status = f"🟡 VISIBLE - Below Lock-On ({DESIGNED_EL}°)"
        status_color = 'orange'
    else:
        status = f"🟢 LOCKED ON - Above {DESIGNED_EL}°"
        status_color = 'green'

    info_text += f"{status}"

    ax2.text(0.05, 0.95, info_text, transform=ax2.transAxes,
             fontsize=11, verticalalignment='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Add status indicator
    ax2.text(0.05, 0.05, status, transform=ax2.transAxes,
             fontsize=14, fontweight='bold', color=status_color,
             verticalalignment='bottom')

    # Add reference to textbook
    ax2.text(0.95, 0.02, 'Based on: Ground Station Design Ch. 4\nEquations 4.28, 5.2, 5.4',
             transform=ax2.transAxes, fontsize=8,
             horizontalalignment='right', verticalalignment='bottom',
             style='italic', color='gray')

    return []

# Create animation
anim = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=num_frames, interval=50,
                              blit=False, repeat=True)

# Save animation (optional)
# anim.save('horizon_plane_animation.gif', writer='pillow', fps=20)

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ANIMATION CONTROLS:")
print("="*60)
print("• Watch the satellite (red star) move along its orbit")
print("• Green arc = Visible portion (0° elevation)")
print("• Orange arc = Lock-on portion (30° elevation)")
print("• Right panel shows real-time measurements")
print("• Green/Orange/Red status indicates communication state")
print("="*60)
