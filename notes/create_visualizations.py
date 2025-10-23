"""
Create professional visualizations for LEO Coverage & Sun Synchronization Study Guide
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Arc
import matplotlib.patches as mpatches

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# Constants
RE = 6371  # Earth radius in km

# Create output directory
import os
output_dir = "study_guide_figures"
os.makedirs(output_dir, exist_ok=True)

# ============================================================================
# FIGURE 1: Coverage Geometry Triangle
# ============================================================================
def create_coverage_geometry():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))

    # Parameters
    H = 800  # altitude
    epsilon = 10  # elevation angle
    r = RE + H

    # Calculate angles
    sin_alpha = (RE / r) * np.cos(np.radians(epsilon))
    alpha = np.degrees(np.arcsin(sin_alpha))
    beta = 90 - epsilon - alpha

    # Calculate slant range
    d = RE * np.sin(np.radians(beta)) / np.sin(np.radians(alpha))

    # Draw Earth (center at origin)
    earth = Circle((0, 0), RE, color='lightblue', ec='navy', linewidth=2, label='Earth')
    ax.add_patch(earth)

    # Ground station position (on Earth's surface)
    gs_angle = np.radians(beta)
    gs_x = RE * np.cos(gs_angle)
    gs_y = RE * np.sin(gs_angle)

    # Satellite position
    sat_x = 0
    sat_y = r

    # Draw lines
    # Earth center to satellite
    ax.plot([0, sat_x], [0, sat_y], 'r-', linewidth=2, label='Altitude H')
    # Earth center to ground station
    ax.plot([0, gs_x], [0, gs_y], 'g-', linewidth=3, label='Earth Radius $R_E$')
    # Ground station to satellite
    ax.plot([gs_x, sat_x], [gs_y, sat_y], 'purple', linewidth=2, label='Slant Range d')

    # Draw angles
    # Beta angle (central angle)
    arc_beta = Arc((0, 0), RE*0.4, RE*0.4, angle=0, theta1=90-beta, theta2=90,
                   color='orange', linewidth=3)
    ax.add_patch(arc_beta)
    ax.text(RE*0.15, RE*0.25, r'$\beta_0$', fontsize=16, color='orange', fontweight='bold')

    # Alpha angle (nadir angle)
    arc_alpha = Arc((sat_x, sat_y), 800, 800, angle=0, theta1=180+beta, theta2=270,
                    color='red', linewidth=3)
    ax.add_patch(arc_alpha)
    ax.text(sat_x-400, sat_y-500, r'$\alpha_0$', fontsize=16, color='red', fontweight='bold')

    # Epsilon angle (elevation angle)
    # Draw horizon line
    horizon_angle = np.radians(90 + beta)
    horizon_len = 1500
    horizon_x = gs_x + horizon_len * np.cos(horizon_angle)
    horizon_y = gs_y + horizon_len * np.sin(horizon_angle)
    ax.plot([gs_x - 500*np.cos(horizon_angle), horizon_x],
            [gs_y - 500*np.sin(horizon_angle), horizon_y],
            'k--', linewidth=2, alpha=0.7, label='Horizon Plane')

    arc_epsilon = Arc((gs_x, gs_y), 1000, 1000,
                      angle=np.degrees(horizon_angle), theta1=0, theta2=epsilon,
                      color='green', linewidth=3)
    ax.add_patch(arc_epsilon)
    ax.text(gs_x+200, gs_y+800, r'$\varepsilon_0$', fontsize=16, color='green', fontweight='bold')

    # Mark points
    ax.plot(0, 0, 'ko', markersize=12, label='Earth Center')
    ax.plot(sat_x, sat_y, 'r^', markersize=15, label='Satellite')
    ax.plot(gs_x, gs_y, 'gs', markersize=12, label='Ground Station')

    # Add labels with values
    ax.text(sat_x+300, sat_y, f'Satellite\n(H={H} km)', fontsize=12,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    ax.text(gs_x+300, gs_y-500, f'Ground Station', fontsize=12,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    # Add formula box
    formula_text = (
        f'Given: H = {H} km, $\\varepsilon_0$ = {epsilon}°\n'
        f'Calculated:\n'
        f'  $\\alpha_0$ = {alpha:.1f}°\n'
        f'  $\\beta_0$ = {beta:.1f}°\n'
        f'  d = {d:.1f} km\n\n'
        f'Formula: $\\varepsilon_0 + \\alpha_0 + \\beta_0 = 90°$'
    )
    ax.text(0.02, 0.98, formula_text, transform=ax.transAxes,
            fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    ax.set_xlim(-8500, 8500)
    ax.set_ylim(-1000, 9000)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right', fontsize=10)
    ax.set_xlabel('Distance (km)', fontsize=12)
    ax.set_ylabel('Distance (km)', fontsize=12)
    ax.set_title('LEO Coverage Geometry: The Coverage Triangle\n' +
                 'Understanding the relationship between elevation, nadir, and central angles',
                 fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{output_dir}/01_coverage_geometry.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: Coverage Geometry Triangle")
    plt.close()

# ============================================================================
# FIGURE 2: Coverage vs Altitude and Elevation
# ============================================================================
def create_coverage_plots():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Data from tables
    altitudes = [600, 800, 1000, 1200]
    elevations = [0, 2, 4, 6, 8, 10]

    # Coverage data
    coverage_data = {
        600: [4.30, 3.63, 3.05, 2.53, 2.08, 1.69],
        800: [5.60, 4.84, 4.16, 3.49, 3.01, 2.54],
        1000: [6.80, 5.95, 5.21, 4.54, 3.91, 3.38],
        1200: [7.95, 7.08, 6.22, 5.48, 4.75, 4.20]
    }

    # Plot 1: Coverage vs Elevation for different altitudes
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    for i, alt in enumerate(altitudes):
        ax1.plot(elevations, coverage_data[alt], 'o-', linewidth=2.5,
                markersize=8, label=f'{alt} km', color=colors[i])

    ax1.set_xlabel('Elevation Angle (degrees)', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Coverage (%)', fontsize=13, fontweight='bold')
    ax1.set_title('Coverage vs Elevation Angle\n(Higher elevation = smaller coverage)',
                  fontsize=14, fontweight='bold')
    ax1.legend(title='Altitude', fontsize=11, title_fontsize=12)
    ax1.grid(True, alpha=0.4)
    ax1.set_xticks(elevations)

    # Add annotation
    ax1.annotate('Trade-off:\nBetter signal quality\nvs\nSmaller coverage area',
                xy=(8, 2.08), xytext=(5, 5.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'),
                fontsize=11, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    # Plot 2: Coverage vs Altitude for different elevations
    for i, elev in enumerate([0, 2, 4, 6, 8, 10]):
        coverage_at_elev = [coverage_data[alt][i] for alt in altitudes]
        ax2.plot(altitudes, coverage_at_elev, 'o-', linewidth=2.5,
                markersize=8, label=f'{elev}°')

    ax2.set_xlabel('Altitude (km)', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Coverage (%)', fontsize=13, fontweight='bold')
    ax2.set_title('Coverage vs Altitude\n(Higher altitude = larger coverage)',
                  fontsize=14, fontweight='bold')
    ax2.legend(title='Elevation', fontsize=11, title_fontsize=12, ncol=2)
    ax2.grid(True, alpha=0.4)
    ax2.set_xticks(altitudes)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/02_coverage_vs_params.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: Coverage vs Altitude and Elevation")
    plt.close()

# ============================================================================
# FIGURE 3: Coverage Belt Visualization
# ============================================================================
def create_coverage_belt():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))

    # Draw Earth
    earth = Circle((0, 0), RE, color='lightblue', ec='navy', linewidth=2)
    ax.add_patch(earth)

    # Satellite orbit
    H = 800
    r = RE + H
    orbit_circle = Circle((0, 0), r, fill=False, ec='red', linewidth=2,
                          linestyle='--', label='Satellite Orbit')
    ax.add_patch(orbit_circle)

    # Show satellite at several positions along orbit
    num_positions = 8
    angles = np.linspace(0, 180, num_positions)

    # Calculate coverage radius at 0 degrees elevation
    d_max = RE * np.sqrt((r/RE)**2 - 1)

    for i, angle in enumerate(angles):
        rad = np.radians(angle)
        sat_x = r * np.cos(rad)
        sat_y = r * np.sin(rad)

        # Draw satellite
        ax.plot(sat_x, sat_y, 'r^', markersize=10, alpha=0.7)

        # Draw coverage circle on Earth
        # Coverage center on Earth below satellite
        coverage_center_angle = angle
        coverage_center_rad = np.radians(coverage_center_angle)
        center_x = RE * np.cos(coverage_center_rad)
        center_y = RE * np.sin(coverage_center_rad)

        # Draw coverage area (simplified as circle on Earth's surface)
        coverage = Circle((sat_x, sat_y), d_max, fill=True,
                         color='yellow', alpha=0.15, ec='orange', linewidth=1.5)
        ax.add_patch(coverage)

    # Show the belt swept
    # Create belt polygon
    belt_inner = RE - d_max/2
    belt_outer = RE + d_max/2
    theta = np.linspace(0, np.pi, 100)

    # Outer arc
    x_outer = belt_outer * np.cos(theta)
    y_outer = belt_outer * np.sin(theta)
    # Inner arc
    x_inner = belt_inner * np.cos(theta)
    y_inner = belt_inner * np.sin(theta)

    # Fill the belt
    ax.fill_between(theta, belt_inner, belt_outer, alpha=0.3, color='green',
                    transform=ax.transData, label=f'Coverage Belt\nWidth ≈ {2*d_max:.0f} km')

    # Add labels
    ax.text(0, -RE-1000, 'Coverage Belt', fontsize=14, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Formula box
    formula_text = (
        f'Coverage Belt Width:\n'
        f'$D_{{BELT}} = 2d_{{max}}$\n\n'
        f'Where:\n'
        f'$d_{{max}} = R_E\\sqrt{{(H+R_E)^2/R_E^2 - 1}}$\n\n'
        f'For H = {H} km:\n'
        f'$d_{{max}}$ = {d_max:.0f} km\n'
        f'$D_{{BELT}}$ = {2*d_max:.0f} km'
    )
    ax.text(0.02, 0.98, formula_text, transform=ax.transAxes,
            fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    ax.set_xlim(-9000, 9000)
    ax.set_ylim(-8000, 9000)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right', fontsize=11)
    ax.set_xlabel('Distance (km)', fontsize=12)
    ax.set_ylabel('Distance (km)', fontsize=12)
    ax.set_title('Coverage Belt: Area Swept by Satellite During One Orbit\n' +
                 'Satellite moves along orbit, coverage area sweeps a belt on Earth',
                 fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{output_dir}/03_coverage_belt.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: Coverage Belt Visualization")
    plt.close()

# ============================================================================
# FIGURE 4: Nodal Regression
# ============================================================================
def create_nodal_regression():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Left plot: Nodal regression vs inclination
    inclinations = np.arange(20, 161, 10)
    altitudes = [7000, 7200, 7400, 7600]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    for i, r in enumerate(altitudes):
        # Calculate nodal regression
        regression = -2.06474e14 * np.cos(np.radians(inclinations)) / (r**3.5)
        ax1.plot(inclinations, regression, 'o-', linewidth=2.5, markersize=7,
                label=f'{r-RE:.0f} km altitude', color=colors[i])

    # Add zero line
    ax1.axhline(y=0, color='k', linestyle='--', linewidth=2, alpha=0.5)
    ax1.axvline(x=90, color='purple', linestyle='--', linewidth=2, alpha=0.5,
               label='i=90° (no regression)')

    # Add sun-sync line
    ax1.axhline(y=0.9856, color='red', linestyle='--', linewidth=2.5,
               label='Sun-sync rate (0.9856°/day)')

    ax1.set_xlabel('Inclination (degrees)', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Nodal Regression (°/day)', fontsize=13, fontweight='bold')
    ax1.set_title('Nodal Regression vs Inclination\n(Only retrograde i>90° can be sun-sync)',
                  fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10, loc='best')
    ax1.grid(True, alpha=0.4)
    ax1.set_xlim(20, 160)

    # Annotations
    ax1.annotate('Prograde\n(westward regression)',
                xy=(45, -3), fontsize=11, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax1.annotate('Retrograde\n(eastward regression)',
                xy=(135, 3), fontsize=11, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    # Right plot: Sun-sync inclination window
    altitudes_range = np.linspace(600, 1200, 50)
    r_range = altitudes_range + RE

    # Calculate inclination for sun-sync
    # From: -2.06474e14 * cos(i) / r^3.5 = 0.9856
    # cos(i) = -0.9856 * r^3.5 / 2.06474e14
    cos_i = -0.9856 * (r_range**3.5) / 2.06474e14
    inclinations_sync = np.degrees(np.arccos(cos_i))

    ax2.plot(altitudes_range, inclinations_sync, 'b-', linewidth=3,
            label='Sun-sync inclination')
    ax2.fill_between(altitudes_range, 97.9, 100.5, alpha=0.3, color='green',
                     label='Sun-sync window\n(97.9° - 100.5°)')

    # Mark key points
    ax2.plot(600, 97.9, 'ro', markersize=12, label='600 km: i=97.9°')
    ax2.plot(1200, 100.5, 'rs', markersize=12, label='1200 km: i=100.5°')

    ax2.set_xlabel('Altitude (km)', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Inclination (degrees)', fontsize=13, fontweight='bold')
    ax2.set_title('Sun-Synchronous Inclination Window\n' +
                  'Required inclination for sun-sync at different altitudes',
                  fontsize=14, fontweight='bold')
    ax2.legend(fontsize=11, loc='best')
    ax2.grid(True, alpha=0.4)
    ax2.set_xlim(600, 1200)
    ax2.set_ylim(97, 101)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/04_nodal_regression.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: Nodal Regression Analysis")
    plt.close()

# ============================================================================
# FIGURE 5: 3D Sun-Synchronous Orbit
# ============================================================================
def create_3d_sun_sync():
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Create Earth
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x_earth = RE * np.outer(np.cos(u), np.sin(v))
    y_earth = RE * np.outer(np.sin(u), np.sin(v))
    z_earth = RE * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x_earth, y_earth, z_earth, color='lightblue', alpha=0.6)

    # Create orbital plane
    H = 800
    r = RE + H
    inclination = 98  # degrees (retrograde)

    # Orbit in inclined plane
    theta = np.linspace(0, 2*np.pi, 100)
    x_orbit = r * np.cos(theta)
    y_orbit = r * np.sin(theta) * np.cos(np.radians(inclination))
    z_orbit = r * np.sin(theta) * np.sin(np.radians(inclination))

    ax.plot(x_orbit, y_orbit, z_orbit, 'r-', linewidth=3, label=f'Sun-sync orbit\n(i={inclination}°)')

    # Equatorial plane
    x_eq = r * 1.2 * np.cos(theta)
    y_eq = r * 1.2 * np.sin(theta)
    z_eq = np.zeros_like(theta)
    ax.plot(x_eq, y_eq, z_eq, 'g--', linewidth=2, alpha=0.5, label='Equatorial plane')

    # Draw Sun direction vector
    sun_distance = r * 2
    ax.quiver(0, 0, 0, sun_distance, 0, 0, color='gold', arrow_length_ratio=0.1,
             linewidth=4, label='To Sun')

    # Draw orbital normal vector
    normal_length = r * 1.5
    normal_x = 0
    normal_y = -normal_length * np.sin(np.radians(inclination))
    normal_z = normal_length * np.cos(np.radians(inclination))
    ax.quiver(0, 0, 0, normal_x, normal_y, normal_z, color='blue',
             arrow_length_ratio=0.1, linewidth=3, label='Orbital normal')

    # Mark satellite position
    sat_pos = 50
    ax.plot([x_orbit[sat_pos]], [y_orbit[sat_pos]], [z_orbit[sat_pos]],
           'r^', markersize=15, label='Satellite')

    # Labels and formatting
    ax.set_xlabel('X (km)', fontsize=11, labelpad=10)
    ax.set_ylabel('Y (km)', fontsize=11, labelpad=10)
    ax.set_zlabel('Z (km)', fontsize=11, labelpad=10)
    ax.set_title('3D View: Sun-Synchronous Orbit\n' +
                 'Orbital plane maintains constant angle with Sun direction',
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=10, loc='upper left')

    # Set viewing angle
    ax.view_init(elev=20, azim=45)

    # Equal aspect ratio
    max_range = r * 1.3
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    plt.tight_layout()
    plt.savefig(f'{output_dir}/05_3d_sun_sync_orbit.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: 3D Sun-Synchronous Orbit")
    plt.close()

# ============================================================================
# FIGURE 6: Handover Process
# ============================================================================
def create_handover_diagram():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))

    # Draw concentric circles for elevation angles
    elevations = [0, 20, 40, 60, 80]
    colors_elev = ['#f0f0f0', '#e0e0e0', '#d0d0d0', '#c0c0c0', '#b0b0b0']

    for i, elev in enumerate(reversed(elevations)):
        circle = Circle((0, 0), (90-elev)*100, fill=True,
                       color=colors_elev[len(elevations)-1-i],
                       ec='gray', linewidth=1, alpha=0.5)
        ax.add_patch(circle)
        if elev in [0, 40]:
            ax.text(0, (90-elev)*100 + 200, f'{elev}° elevation',
                   ha='center', fontsize=11, fontweight='bold')

    # Mark center (user)
    ax.plot(0, 0, 'ko', markersize=20, label='User/Ground Station', zorder=5)

    # Draw three satellite orbits
    # Orbit 1 - Low pass (no communication)
    theta1 = np.linspace(180, 360, 50)
    r1 = np.linspace(3000, 3000, 50)
    x1 = r1 * np.cos(np.radians(theta1))
    y1 = r1 * np.sin(np.radians(theta1))
    ax.plot(x1, y1, 'gray', linewidth=3, linestyle='--', alpha=0.5, label='Orbit 1 (no comm)')
    ax.text(3000, -500, 'Max El\n21°', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))

    # Orbit 2 - Good pass
    theta2 = np.linspace(150, 30, 100)
    r2 = np.linspace(7000, 7000, 100)
    x2 = r2 * np.cos(np.radians(theta2))
    y2 = r2 * np.sin(np.radians(theta2))
    ax.plot(x2, y2, 'blue', linewidth=4, label='Orbit 2 (SAT A)')

    # Mark key points for Orbit 2
    # AOS(40) - point A
    idx_aos2 = 20
    ax.plot(x2[idx_aos2], y2[idx_aos2], 'go', markersize=15, zorder=5)
    ax.text(x2[idx_aos2]-500, y2[idx_aos2]+500, 'A: AOS(40°)\nSAT A enters\nComm starts',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    # Max-El
    idx_max2 = 50
    ax.plot(x2[idx_max2], y2[idx_max2], 'b^', markersize=18, zorder=5)
    ax.text(x2[idx_max2]+500, y2[idx_max2]+500, 'Max El\n58°', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    # LOS(40) - point B (handover point!)
    idx_los2 = 80
    ax.plot(x2[idx_los2], y2[idx_los2], 'ro', markersize=15, zorder=5)
    ax.text(x2[idx_los2]+500, y2[idx_los2]-500, 'B: LOS(40°)\nSAT A exits\n⚡HANDOVER⚡',
           fontsize=10, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.9))

    # Orbit 3 - Good pass (handover from Orbit 2)
    theta3 = np.linspace(345, 125, 100)
    r3 = np.linspace(7000, 7000, 100)
    x3 = r3 * np.cos(np.radians(theta3))
    y3 = r3 * np.sin(np.radians(theta3))
    ax.plot(x3, y3, 'red', linewidth=4, label='Orbit 3 (SAT B)')

    # Mark key points for Orbit 3
    # AOS(40) - point B (same as LOS for Orbit 2!)
    idx_aos3 = 20
    ax.plot(x3[idx_aos3], y3[idx_aos3], 'go', markersize=15, zorder=5)
    ax.text(x3[idx_aos3]-1000, y3[idx_aos3], '←B: AOS(40°)\nSAT B enters',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    # Max-El
    idx_max3 = 55
    ax.plot(x3[idx_max3], y3[idx_max3], 'r^', markersize=18, zorder=5)
    ax.text(x3[idx_max3]-700, y3[idx_max3], 'Max El 63°', ha='center', fontsize=10,
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

    # LOS(40) - point C
    idx_los3 = 85
    ax.plot(x3[idx_los3], y3[idx_los3], 'rs', markersize=15, zorder=5)
    ax.text(x3[idx_los3]+500, y3[idx_los3]+800, 'C: LOS(40°)\nSAT B exits\nComm ends',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Draw communication periods
    ax.annotate('', xy=(x2[idx_max2], y2[idx_max2]),
                xytext=(x2[idx_aos2], y2[idx_aos2]),
                arrowprops=dict(arrowstyle='<->', lw=3, color='blue'))
    ax.text(x2[35], y2[35]+1000, 'Communication\nwith SAT A', fontsize=11,
           color='blue', fontweight='bold')

    ax.annotate('', xy=(x3[idx_los3], y3[idx_los3]),
                xytext=(x3[idx_max3], y3[idx_max3]),
                arrowprops=dict(arrowstyle='<->', lw=3, color='red'))
    ax.text(x3[70]-1000, y3[70], 'Communication\nwith SAT B', fontsize=11,
           color='red', fontweight='bold')

    # Explanation box
    explanation = (
        'Handover Process:\n\n'
        '1. User communicates with SAT A (Orbit 2)\n'
        '   from point A to B\n\n'
        '2. At point B, SAT A leaves 40° horizon\n\n'
        '3. At same point B, SAT B enters 40° horizon\n\n'
        '4. SAT A and SAT B communicate via ISL\n'
        '   (Intersatellite Link)\n\n'
        '5. User seamlessly handed to SAT B\n\n'
        '6. User continues communication A→B→C\n'
        '   with NO INTERRUPTION!'
    )
    ax.text(0.02, 0.98, explanation, transform=ax.transAxes,
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))

    # Compass
    ax.text(0, 9200, 'N', ha='center', fontsize=16, fontweight='bold')
    ax.text(0, -9200, 'S', ha='center', fontsize=16, fontweight='bold')
    ax.text(9200, 0, 'E', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(-9200, 0, 'W', ha='center', va='center', fontsize=16, fontweight='bold')

    ax.set_xlim(-10000, 10000)
    ax.set_ylim(-10000, 10000)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower left', fontsize=11)
    ax.set_title('Handover-Takeover Process: Continuous Service via Constellation\n' +
                 '(Radar View from Ground Station)', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{output_dir}/06_handover_process.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: Handover Process Diagram")
    plt.close()

# ============================================================================
# FIGURE 7: Perigee Deviation
# ============================================================================
def create_perigee_deviation():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))

    # Draw Earth
    earth = Circle((0, 0), RE, color='lightblue', ec='navy', linewidth=2)
    ax.add_patch(earth)

    # Original orbit (elliptical for demonstration)
    a = 7200  # semi-major axis
    e = 0.05  # small eccentricity for visualization
    b = a * np.sqrt(1 - e**2)

    # Original orbit
    theta = np.linspace(0, 2*np.pi, 200)
    r_orig = a * (1 - e**2) / (1 + e * np.cos(theta))
    x_orig = r_orig * np.cos(theta)
    y_orig = r_orig * np.sin(theta)
    ax.plot(x_orig, y_orig, 'b-', linewidth=3, label='Original orbit (t=0)')

    # Deviated orbit (rotated by delta-omega)
    delta_omega = np.radians(12)  # 12 degrees deviation (typical for sun-sync)
    x_dev = r_orig * np.cos(theta + delta_omega)
    y_dev = r_orig * np.sin(theta + delta_omega)
    ax.plot(x_dev, y_dev, 'r--', linewidth=3, label=f'Deviated orbit (after N orbits)')

    # Mark perigee points
    perigee_idx = np.argmin(r_orig)
    ax.plot(x_orig[perigee_idx], y_orig[perigee_idx], 'bo', markersize=15,
           label='Original perigee', zorder=5)
    ax.plot(x_dev[perigee_idx], y_dev[perigee_idx], 'ro', markersize=15,
           label='Deviated perigee', zorder=5)

    # Draw line of nodes (equatorial plane intersection)
    ax.plot([-a*1.3, a*1.3], [0, 0], 'g-', linewidth=3, alpha=0.7,
           label='Line of nodes (N-S)')
    ax.text(a*1.1, -500, 'N', fontsize=14, fontweight='bold', color='green')
    ax.text(-a*1.1, -500, 'S', fontsize=14, fontweight='bold', color='green')

    # Draw argument of perigee angles
    arc_orig = Arc((0, 0), a*0.5, a*0.5, angle=0, theta1=0, theta2=np.degrees(0),
                   color='blue', linewidth=3)
    ax.add_patch(arc_orig)
    ax.text(a*0.3, a*0.15, r'$\omega_0$', fontsize=16, color='blue', fontweight='bold')

    arc_dev = Arc((0, 0), a*0.7, a*0.7, angle=0, theta1=0,
                  theta2=np.degrees(delta_omega),
                  color='red', linewidth=3)
    ax.add_patch(arc_dev)
    ax.text(a*0.4, a*0.25, r'$\omega_0 + \Delta\omega$', fontsize=14,
           color='red', fontweight='bold')

    # Draw delta-omega arc
    ax.annotate('', xy=(x_orig[perigee_idx]*0.9, y_orig[perigee_idx]*0.9),
                xytext=(x_dev[perigee_idx]*0.9, y_dev[perigee_idx]*0.9),
                arrowprops=dict(arrowstyle='<->', lw=3, color='purple'))
    ax.text(x_orig[perigee_idx]*0.6, y_orig[perigee_idx]*0.8,
           r'$\Delta\omega$' + f'\n≈12°/orbit',
           fontsize=13, color='purple', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    # Formula box
    formula_text = (
        'Perigee Deviation for Sun-Sync LEO:\n\n'
        r'$\Delta\omega = 0.29\left(\frac{R_E}{a}\right)[4 - 5\sin^2 i]$' + '\n\n'
        'For sun-sync orbits (i = 97.9° - 100.5°):\n'
        '• Always NEGATIVE (opposite to motion)\n'
        '• Range: 10.3\' to 13.1\' per orbit\n\n'
        'Major axis rotates within orbital plane\n'
        'due to Earth\'s equatorial bulge'
    )
    ax.text(0.02, 0.98, formula_text, transform=ax.transAxes,
            fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    # Note about circular orbits
    note = (
        'Note: Shown as ellipse for clarity.\n'
        'LEO orbits are nearly circular (e≈0),\n'
        'but deviation still occurs!'
    )
    ax.text(0.98, 0.02, note, transform=ax.transAxes,
            fontsize=10, ha='right', va='bottom',
            bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.8))

    ax.set_xlim(-9000, 9000)
    ax.set_ylim(-9000, 9000)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right', fontsize=10)
    ax.set_xlabel('Distance (km)', fontsize=12)
    ax.set_ylabel('Distance (km)', fontsize=12)
    ax.set_title('Orbital Perigee Deviation\n' +
                 'Major axis rotates due to Earth\'s oblateness (in same orbital plane)',
                 fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{output_dir}/07_perigee_deviation.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: Perigee Deviation Diagram")
    plt.close()

# ============================================================================
# RUN ALL VISUALIZATIONS
# ============================================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("Creating Study Guide Visualizations")
    print("="*60 + "\n")

    create_coverage_geometry()
    create_coverage_plots()
    create_coverage_belt()
    create_nodal_regression()
    create_3d_sun_sync()
    create_handover_diagram()
    create_perigee_deviation()

    print("\n" + "="*60)
    print(f"[OK] All visualizations created successfully!")
    print(f"[OK] Saved to folder: {output_dir}/")
    print("="*60 + "\n")
