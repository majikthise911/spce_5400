#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 4: Lock-On Percentage Visualization
Shows the geometry of satellite visibility and 30 degree designed elevation lock-on
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
R_E = 6371  # km (Earth radius)
H = 1000    # km (satellite altitude)
r = R_E + H  # orbital radius

# Question 3 results: Full visibility (0 deg elevation)
alpha_0_max = np.deg2rad(59.75)  # maximum nadir angle
beta_0_max = np.deg2rad(30.25)   # maximum central angle
gamma_visible = np.deg2rad(60.5) # total visibility arc

# Question 4 results: Designed elevation (30 deg)
epsilon_designed = 30  # degrees
alpha_0_designed = np.deg2rad(48.45)  # nadir angle at 30 deg elevation
beta_0_designed = np.deg2rad(11.55)   # central angle at 30 deg elevation
gamma_designed = np.deg2rad(23.1)     # designed lock-on arc

# Time calculations
T_orbit = 6295.5  # seconds (orbital period)
t_visible = 1058  # seconds (visible time)
t_locked = 404    # seconds (lock-on time)
percent_locked = 38.2  # percent

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ===== LEFT PLOT: Geometry visualization =====
ax1.set_aspect('equal')
ax1.set_title('Satellite Visibility Geometry\n(Overhead Pass)', fontsize=14, fontweight='bold')

# Draw Earth
earth = plt.Circle((0, 0), R_E, color='lightblue', label='Earth', zorder=1)
ax1.add_patch(earth)

# Draw ground station (at top of Earth for overhead pass)
gs_angle = np.pi/2  # ground station at top (North Pole for visualization)
gs_x = R_E * np.cos(gs_angle)
gs_y = R_E * np.sin(gs_angle)
ax1.plot(gs_x, gs_y, 'r^', markersize=15, label='Ground Station', zorder=5)

# Draw orbital circle
orbit_circle = plt.Circle((0, 0), r, fill=False, color='gray',
                          linestyle='--', linewidth=1, label='Satellite Orbit')
ax1.add_patch(orbit_circle)

# Draw satellite positions for full visibility arc (0 deg elevation)
# Satellite sweeps from -beta_0_max to +beta_0_max
satellite_angles_full = np.linspace(gs_angle - beta_0_max,
                                    gs_angle + beta_0_max, 50)
sat_x_full = r * np.cos(satellite_angles_full)
sat_y_full = r * np.sin(satellite_angles_full)
ax1.plot(sat_x_full, sat_y_full, 'b-', linewidth=3,
         label=f'Visible Arc (0° elev)\nγ = {np.rad2deg(gamma_visible):.1f}°', zorder=2)

# Mark AOS and LOS positions (0 deg elevation)
aos_angle = gs_angle - beta_0_max
los_angle = gs_angle + beta_0_max
ax1.plot(r * np.cos(aos_angle), r * np.sin(aos_angle), 'bo',
         markersize=10, label='AOS (0° elev)', zorder=4)
ax1.plot(r * np.cos(los_angle), r * np.sin(los_angle), 'bs',
         markersize=10, label='LOS (0° elev)', zorder=4)

# Draw satellite positions for designed lock-on arc (30 deg elevation)
satellite_angles_designed = np.linspace(gs_angle - beta_0_designed,
                                        gs_angle + beta_0_designed, 50)
sat_x_designed = r * np.cos(satellite_angles_designed)
sat_y_designed = r * np.sin(satellite_angles_designed)
ax1.plot(sat_x_designed, sat_y_designed, 'g-', linewidth=5,
         label=f'Lock-On Arc (30° elev)\nγ = {np.rad2deg(gamma_designed):.1f}°', zorder=3)

# Mark 30 deg elevation positions
lock_start_angle = gs_angle - beta_0_designed
lock_end_angle = gs_angle + beta_0_designed
ax1.plot(r * np.cos(lock_start_angle), r * np.sin(lock_start_angle), 'go',
         markersize=10, label='Lock-On Start (30°)', zorder=4)
ax1.plot(r * np.cos(lock_end_angle), r * np.sin(lock_end_angle), 'gs',
         markersize=10, label='Lock-On End (30°)', zorder=4)

# Mark zenith position
ax1.plot(r * np.cos(gs_angle), r * np.sin(gs_angle), 'r*',
         markersize=20, label='Zenith (90° elev)', zorder=6)

# Draw lines from ground station to key positions
ax1.plot([gs_x, r * np.cos(aos_angle)], [gs_y, r * np.sin(aos_angle)],
         'b--', alpha=0.3, linewidth=1)
ax1.plot([gs_x, r * np.cos(lock_start_angle)], [gs_y, r * np.sin(lock_start_angle)],
         'g--', alpha=0.5, linewidth=1)

# Labels and formatting
ax1.set_xlabel('Distance (km)', fontsize=11)
ax1.set_ylabel('Distance (km)', fontsize=11)
ax1.legend(loc='upper left', fontsize=8, framealpha=0.9)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-8500, 8500)
ax1.set_ylim(-8500, 8500)

# Add text annotations
ax1.text(0, -R_E*0.7, 'Earth\nRadius = 6371 km',
         ha='center', va='center', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax1.text(0, r*0.85, f'Satellite Altitude\n{H} km',
         ha='center', va='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# ===== RIGHT PLOT: Time/Percentage visualization =====
categories = ['Full Visible\nPass\n(0° elevation)',
              'Lock-On Time\n(≥30° elevation)',
              'Below 30°\nElevation']
times = [t_visible, t_locked, t_visible - t_locked]
colors = ['lightblue', 'lightgreen', 'lightcoral']
percentages = [100, percent_locked, 100 - percent_locked]

# Create bar chart
bars = ax2.bar(categories, times, color=colors, edgecolor='black', linewidth=2)

# Add value labels on bars
for i, (bar, time, pct) in enumerate(zip(bars, times, percentages)):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{time} sec\n({pct:.1f}%)',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

ax2.set_ylabel('Time (seconds)', fontsize=12)
ax2.set_title('Overhead Pass Time Breakdown', fontsize=14, fontweight='bold')
ax2.set_ylim(0, t_visible * 1.2)
ax2.grid(True, axis='y', alpha=0.3)

# Add summary text box
summary_text = f"""Key Results:
• Total visible time: {t_visible} sec (17 min 38 sec)
• Lock-on time (≥30°): {t_locked} sec (6 min 44 sec)
• Lock-on percentage: {percent_locked}%

Angular Arcs:
• Visible arc (γ): {np.rad2deg(gamma_visible):.1f}°
• Lock-on arc (γ_D): {np.rad2deg(gamma_designed):.1f}°
• Ratio: {np.rad2deg(gamma_designed)/np.rad2deg(gamma_visible)*100:.1f}%
"""

ax2.text(0.5, 0.02, summary_text, transform=ax2.transAxes,
         fontsize=10, verticalalignment='bottom', horizontalalignment='center',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Overall title
fig.suptitle('Question 4: Lock-On Percentage for 30° Designed Elevation',
             fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save figure
plt.savefig('q4_lockon_visualization.png', dpi=300, bbox_inches='tight')
print("Plot saved as 'q4_lockon_visualization.png'")

# Print summary to console
print("\n" + "="*60)
print("QUESTION 4 SUMMARY")
print("="*60)
print(f"Designed Elevation:        30°")
print(f"Total Visible Time:        {t_visible} sec ({t_visible/60:.1f} min)")
print(f"Lock-On Time (≥30°):       {t_locked} sec ({t_locked/60:.1f} min)")
print(f"Time Below 30°:            {t_visible - t_locked} sec")
print(f"\nLock-On Percentage:        {percent_locked}%")
print(f"\nVisible Arc (0° elev):     {np.rad2deg(gamma_visible):.1f}°")
print(f"Lock-On Arc (30° elev):    {np.rad2deg(gamma_designed):.1f}°")
print(f"Arc Ratio:                 {np.rad2deg(gamma_designed)/np.rad2deg(gamma_visible)*100:.1f}%")
print("="*60)

plt.show()
