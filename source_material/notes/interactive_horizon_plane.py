"""
Interactive visualization with slider control to manually position satellite
and observe how elevation angle, slant range, and horizon planes relate.

Features:
- Slider to move satellite along orbit
- Real-time angle calculations
- Color-coded communication zones
- Geometric angle visualization (nadir, central, elevation)
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# Constants (from Chapter 4)
R_E = 6371  # Earth radius km
H = 1000    # Satellite altitude km
r = R_E + H  # Orbital radius

# Designed elevation angle
DESIGNED_EL = 30  # degrees

# Ground station location
theta_gs = 0  # degrees
gs_x = R_E * np.cos(np.radians(theta_gs))
gs_y = R_E * np.sin(np.radians(theta_gs))

# Calculate key angles
alpha_0_max = np.degrees(np.arcsin(R_E / r))
gamma_max = 2 * alpha_0_max

sin_alpha_30 = (R_E / r) * np.cos(np.radians(DESIGNED_EL))
alpha_30 = np.degrees(np.arcsin(sin_alpha_30))
beta_30 = 90 - DESIGNED_EL - alpha_30
gamma_30 = 2 * beta_30

def calculate_elevation(sat_x, sat_y, gs_x, gs_y):
    """Calculate elevation angle from ground station to satellite"""
    dx = sat_x - gs_x
    dy = sat_y - gs_y
    gsx_norm = gs_x
    gsy_norm = gs_y

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

def calculate_nadir_angle(sat_x, sat_y, gs_x, gs_y):
    """Calculate nadir angle (angle at satellite between Earth center and ground station)"""
    # Vector from satellite to Earth center
    vec_sc_x = -sat_x
    vec_sc_y = -sat_y

    # Vector from satellite to ground station
    vec_sg_x = gs_x - sat_x
    vec_sg_y = gs_y - sat_y

    # Calculate angle between vectors
    dot = vec_sc_x * vec_sg_x + vec_sc_y * vec_sg_y
    mag_sc = np.sqrt(vec_sc_x**2 + vec_sc_y**2)
    mag_sg = np.sqrt(vec_sg_x**2 + vec_sg_y**2)

    if mag_sc == 0 or mag_sg == 0:
        return 0

    cos_angle = dot / (mag_sc * mag_sg)
    cos_angle = np.clip(cos_angle, -1, 1)
    nadir = np.degrees(np.arccos(cos_angle))
    return nadir

def calculate_central_angle(sat_x, sat_y, gs_x, gs_y):
    """Calculate central angle at Earth center"""
    # Vectors from Earth center
    mag_sat = np.sqrt(sat_x**2 + sat_y**2)
    mag_gs = np.sqrt(gs_x**2 + gs_y**2)

    if mag_sat == 0 or mag_gs == 0:
        return 0

    dot = sat_x * gs_x + sat_y * gs_y
    cos_angle = dot / (mag_sat * mag_gs)
    cos_angle = np.clip(cos_angle, -1, 1)
    central = np.degrees(np.arccos(cos_angle))
    return central

# Setup figure - much larger with more spacing to fit all content
fig = plt.figure(figsize=(24, 14))
gs_layout = fig.add_gridspec(3, 2, height_ratios=[5, 5, 0.8], hspace=0.35, wspace=0.35,
                              left=0.08, right=0.98, top=0.94, bottom=0.08)

ax_main = fig.add_subplot(gs_layout[0:2, 0])  # Main geometric plot
ax_angles = fig.add_subplot(gs_layout[0, 1])  # Angle diagram
ax_info = fig.add_subplot(gs_layout[1, 1])    # Information display
ax_slider = fig.add_subplot(gs_layout[2, :])  # Slider

fig.suptitle('Interactive LEO Satellite Pass Visualization\n' +
             'Use slider to move satellite and observe geometric relationships',
             fontsize=16, fontweight='bold')

# Initial satellite position
initial_theta = 0
# Create slider without valstep to allow continuous dragging
theta_slider = Slider(ax_slider, 'Satellite Position (°)',
                     -gamma_max/2 - 30, gamma_max/2 + 30,
                     valinit=initial_theta,
                     color='red',
                     track_color='lightgray')

def update(val):
    """Update plots when slider changes"""
    theta_sat = theta_slider.val

    # Current satellite position
    sat_x = r * np.cos(np.radians(theta_sat))
    sat_y = r * np.sin(np.radians(theta_sat))

    # Calculate angles
    elevation = calculate_elevation(sat_x, sat_y, gs_x, gs_y)
    nadir = calculate_nadir_angle(sat_x, sat_y, gs_x, gs_y)
    central = calculate_central_angle(sat_x, sat_y, gs_x, gs_y)
    d = np.sqrt((sat_x - gs_x)**2 + (sat_y - gs_y)**2)

    # Clear and redraw main plot
    ax_main.clear()
    ax_main.set_aspect('equal')
    ax_main.set_xlim(-R_E*1.2, r*1.2)
    ax_main.set_ylim(-r*1.2, r*1.2)  # Much taller to show full orbit
    ax_main.set_xlabel('Distance (km)', fontsize=11)
    ax_main.set_ylabel('Height (km)', fontsize=11)
    ax_main.set_title('Geometric View', fontsize=12, fontweight='bold')
    ax_main.grid(True, alpha=0.3)

    # Draw Earth
    theta_earth = np.linspace(0, 2*np.pi, 100)
    x_earth = R_E * np.cos(theta_earth)
    y_earth = R_E * np.sin(theta_earth)
    ax_main.fill(x_earth, y_earth, color='lightblue', alpha=0.5)
    ax_main.plot(x_earth, y_earth, 'b-', linewidth=2)

    # Draw orbit
    theta_orbit = np.linspace(0, 2*np.pi, 100)
    x_orbit = r * np.cos(theta_orbit)
    y_orbit = r * np.sin(theta_orbit)
    ax_main.plot(x_orbit, y_orbit, 'gray', linestyle='--', linewidth=1, alpha=0.3)

    # Visible arc (0° elevation) - GREEN
    theta_visible = np.linspace(np.radians(-gamma_max/2), np.radians(gamma_max/2), 50)
    x_visible = r * np.cos(theta_visible)
    y_visible = r * np.sin(theta_visible)
    ax_main.plot(x_visible, y_visible, 'g-', linewidth=4, alpha=0.6, label='Visible (0°)')

    # Designed arc (30° elevation) - ORANGE
    theta_designed = np.linspace(np.radians(-gamma_30/2), np.radians(gamma_30/2), 50)
    x_designed = r * np.cos(theta_designed)
    y_designed = r * np.sin(theta_designed)
    ax_main.plot(x_designed, y_designed, 'orange', linewidth=4, alpha=0.8, label=f'Lock-On ({DESIGNED_EL}°)')

    # AOS/LOS markers
    aos_x = r * np.cos(np.radians(-gamma_max/2))
    aos_y = r * np.sin(np.radians(-gamma_max/2))
    los_x = r * np.cos(np.radians(gamma_max/2))
    los_y = r * np.sin(np.radians(gamma_max/2))
    ax_main.plot(aos_x, aos_y, 'go', markersize=10, label='AOS (0°)', zorder=5)
    ax_main.plot(los_x, los_y, 'ro', markersize=10, label='LOS (0°)', zorder=5)
    ax_main.text(aos_x-500, aos_y-500, 'AOS', fontsize=9, color='green', fontweight='bold')
    ax_main.text(los_x+300, los_y-500, 'LOS', fontsize=9, color='red', fontweight='bold')

    # Ground station
    ax_main.plot(gs_x, gs_y, 'k^', markersize=18, label='Ground Station', zorder=10)
    ax_main.text(gs_x+200, gs_y-500, 'GS', fontsize=10, fontweight='bold')

    # Current satellite
    sat_color = 'red' if elevation < 0 else ('orange' if elevation < DESIGNED_EL else 'green')
    ax_main.plot(sat_x, sat_y, '*', color=sat_color, markersize=25,
                label='Satellite', zorder=10, markeredgecolor='black', markeredgewidth=1)

    # Slant range
    ax_main.plot([gs_x, sat_x], [gs_y, sat_y], color=sat_color,
                linestyle='--', linewidth=2.5, alpha=0.8, label=f'd = {d:.0f} km')

    # Lines for angle visualization
    ax_main.plot([0, sat_x], [0, sat_y], 'purple', linestyle=':', linewidth=1.5, alpha=0.5)
    ax_main.plot([0, gs_x], [0, gs_y], 'black', linestyle=':', linewidth=1.5, alpha=0.5)

    # Horizon planes
    horizon_angle = np.radians(theta_gs + 90)
    horizon_length = R_E * 1.5
    horizon_x1 = gs_x - horizon_length * np.cos(horizon_angle)
    horizon_y1 = gs_y - horizon_length * np.sin(horizon_angle)
    horizon_x2 = gs_x + horizon_length * np.cos(horizon_angle)
    horizon_y2 = gs_y + horizon_length * np.sin(horizon_angle)
    ax_main.plot([horizon_x1, horizon_x2], [horizon_y1, horizon_y2],
                'g--', linewidth=1.5, alpha=0.5)

    ax_main.legend(loc='upper right', fontsize=9)

    # === ANGLE DIAGRAM (Top Right) ===
    ax_angles.clear()
    ax_angles.set_aspect('equal')
    ax_angles.set_xlim(-1.5, 1.5)
    ax_angles.set_ylim(-0.5, 1.5)
    ax_angles.axis('off')
    ax_angles.set_title('Geometric Angles\n(ε + α + β = 90°)', fontsize=12, fontweight='bold')

    # Draw simplified triangle showing angles
    # Earth center at origin
    ax_angles.plot(0, 0, 'ko', markersize=8)
    ax_angles.text(-0.2, -0.15, 'O\n(Earth\nCenter)', fontsize=8, ha='center')

    # Ground station
    gs_draw_x = 1.0
    gs_draw_y = 0.0
    ax_angles.plot(gs_draw_x, gs_draw_y, 'k^', markersize=12)
    ax_angles.text(gs_draw_x, -0.2, 'GS', fontsize=9, ha='center', fontweight='bold')

    # Satellite
    # Position based on actual angles
    sat_draw_angle = np.radians(90 - central)  # Convert to drawing angle
    sat_draw_x = 1.2 * np.cos(sat_draw_angle)
    sat_draw_y = 1.2 * np.sin(sat_draw_angle)
    ax_angles.plot(sat_draw_x, sat_draw_y, '*', color=sat_color, markersize=15)
    ax_angles.text(sat_draw_x, sat_draw_y + 0.15, 'SAT', fontsize=9, ha='center', fontweight='bold')

    # Draw triangle
    ax_angles.plot([0, gs_draw_x], [0, gs_draw_y], 'k-', linewidth=2)
    ax_angles.plot([0, sat_draw_x], [0, sat_draw_y], 'purple', linewidth=2)
    ax_angles.plot([gs_draw_x, sat_draw_x], [gs_draw_y, sat_draw_y], color=sat_color, linewidth=2)

    # Draw horizon line
    ax_angles.plot([gs_draw_x - 0.5, gs_draw_x + 0.5], [0, 0], 'g--', linewidth=1.5, alpha=0.7)

    # Label angles
    ax_angles.text(0.15, 0.15, f'β={central:.1f}°', fontsize=10, color='blue', fontweight='bold')
    ax_angles.text(sat_draw_x - 0.15, sat_draw_y - 0.15, f'α={nadir:.1f}°',
                  fontsize=10, color='purple', fontweight='bold')
    ax_angles.text(gs_draw_x + 0.3, 0.15, f'ε={elevation:.1f}°',
                  fontsize=10, color=sat_color, fontweight='bold')

    # Verification
    sum_angles = elevation + nadir + central
    ax_angles.text(0, -0.45, f'Verification: ε + α + β = {sum_angles:.1f}° ≈ 90°',
                  fontsize=9, ha='center', style='italic',
                  bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    # === INFORMATION DISPLAY (Bottom Right) ===
    ax_info.clear()
    ax_info.axis('off')

    # Determine status
    if elevation < 0:
        status = "⚫ BELOW HORIZON\nNo Signal"
        status_color = 'red'
    elif elevation < DESIGNED_EL:
        status = f"🟡 VISIBLE BUT NOT LOCKED\nBelow {DESIGNED_EL}° threshold"
        status_color = 'orange'
    else:
        status = f"🟢 LOCKED ON\nAbove {DESIGNED_EL}° elevation"
        status_color = 'green'

    info_text = f"""
╔═══════════════════════════════════════╗
║  CURRENT MEASUREMENTS                 ║
╠═══════════════════════════════════════╣
║  Elevation Angle (ε):  {elevation:6.2f}°    ║
║  Nadir Angle (α):      {nadir:6.2f}°    ║
║  Central Angle (β):    {central:6.2f}°    ║
║  Slant Range (d):      {d:6.0f} km   ║
╠═══════════════════════════════════════╣
║  GEOMETRIC CONSTANTS                  ║
╠═══════════════════════════════════════╣
║  Altitude (H):         {H:6} km   ║
║  Earth Radius (R_E):   {R_E:6} km   ║
║  Orbital Radius (r):   {r:6} km   ║
╠═══════════════════════════════════════╣
║  IDEAL HORIZON (0°)                   ║
╠═══════════════════════════════════════╣
║  Max Nadir (α_max):    {alpha_0_max:6.2f}°    ║
║  Visibility Arc (γ):   {gamma_max:6.2f}°    ║
╠═══════════════════════════════════════╣
║  DESIGNED HORIZON ({DESIGNED_EL}°)              ║
╠═══════════════════════════════════════╣
║  Design Nadir (α_D):   {alpha_30:6.2f}°    ║
║  Design Central (β_D): {beta_30:6.2f}°    ║
║  Lock-On Arc (γ_D):    {gamma_30:6.2f}°    ║
╚═══════════════════════════════════════╝
"""

    ax_info.text(0.05, 0.95, info_text, transform=ax_info.transAxes,
                fontsize=10, verticalalignment='top', family='monospace',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))

    ax_info.text(0.5, 0.02, status, transform=ax_info.transAxes,
                fontsize=13, fontweight='bold', color=status_color,
                ha='center', va='bottom',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

    # Chapter reference
    ax_info.text(0.98, 0.02, 'Ch 4: Eqs 4.28, 5.2, 5.4',
                transform=ax_info.transAxes, fontsize=7,
                ha='right', va='bottom', style='italic', color='gray')

    fig.canvas.draw_idle()

# Connect slider to update function
theta_slider.on_changed(update)

# Initial draw
update(initial_theta)

plt.show()

print("\n" + "="*60)
print("INTERACTIVE CONTROLS:")
print("="*60)
print("• Use the slider to move the satellite along its orbit")
print("• Watch how elevation angle changes")
print("• Observe when satellite enters/exits lock-on zone")
print("• Top-right shows geometric angle relationships")
print("• Bottom-right displays real-time measurements")
print("• Color coding: Green=Locked, Orange=Visible, Red=Hidden")
print("="*60)
print("\nKEY CONCEPTS:")
print("  ε = Elevation angle (at ground station)")
print("  α = Nadir angle (at satellite)")
print("  β = Central angle (at Earth center)")
print("  Relationship: ε + α + β = 90° (from Ch 4.2)")
print("="*60)
