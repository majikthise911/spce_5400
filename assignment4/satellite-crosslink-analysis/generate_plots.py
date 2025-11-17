"""
Generate visualizations for Optical vs RF Crosslink Trade Study
Assignment 4 - SpCE 5400

This script generates publication-quality plots for the submission document.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, FancyArrowPatch
from matplotlib.patches import Rectangle
import os

# Create output directory for plots
output_dir = "outputs/figures"
os.makedirs(output_dir, exist_ok=True)

# Set style for professional plots
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 14

# Color scheme
color_optical = '#2E86AB'  # Blue
color_rf = '#A23B72'       # Purple/Magenta
color_threshold = '#F18F01' # Orange
color_good = '#06A77D'     # Green
color_bad = '#D62246'      # Red


# ==============================================================================
# PLOT 1: Link Margin Comparison Bar Chart
# ==============================================================================
def plot_link_margin_comparison():
    fig, ax = plt.subplots(figsize=(10, 6))

    technologies = ['Optical\n(Laser)', 'RF\n(Ka-band)']
    margins = [25.66, 2.8]
    colors = [color_optical, color_rf]

    bars = ax.bar(technologies, margins, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add horizontal line at 3 dB minimum
    ax.axhline(y=3, color=color_threshold, linestyle='--', linewidth=2, label='Minimum Required (3 dB)')

    # Add value labels on bars
    for i, (bar, margin) in enumerate(zip(bars, margins)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{margin:.2f} dB\n({10**(margin/10):.1f}× margin)',
                ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Add ratio annotation
    ax.annotate('', xy=(0, 25.66), xytext=(1, 2.8),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(0.5, 14, '9.2× more margin', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    ax.set_ylabel('Link Margin (dB)', fontsize=13, fontweight='bold')
    ax.set_title('Link Margin Comparison: Optical vs RF Crosslinks\n250 km Range, 1 Gbps Data Rate',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_ylim(0, 30)
    ax.legend(loc='upper right', fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/01_link_margin_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 01_link_margin_comparison.png")


# ==============================================================================
# PLOT 2: Pointing Requirement Comparison
# ==============================================================================
def plot_pointing_comparison():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Data in microradians
    optical_pointing = 8.0      # μrad (half-power beamwidth)
    rf_pointing = 38200.0        # μrad (2.19 degrees converted)

    # Use log scale for better visualization
    technologies = ['Optical\n(Laser)', 'RF\n(Ka-band)']
    pointings = [optical_pointing, rf_pointing]
    colors = [color_optical, color_rf]

    bars = ax.barh(technologies, pointings, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    # Add value labels
    ax.text(optical_pointing + 500, 0, f'{optical_pointing:.1f} μrad\n(0.00046°)\n1.6 arcsec',
            va='center', fontsize=11, fontweight='bold')
    ax.text(rf_pointing + 500, 1, f'{rf_pointing:.0f} μrad\n(2.19°)\n7,880 arcsec',
            va='center', fontsize=11, fontweight='bold')

    # Add ratio annotation
    ratio = rf_pointing / optical_pointing
    ax.text(20000, 0.5, f'RF is {ratio:.0f}× easier to point', ha='center', fontsize=12,
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8),
            fontweight='bold')

    ax.set_xlabel('Pointing Requirement (microradians, log scale)', fontsize=13, fontweight='bold')
    ax.set_title('Pointing Accuracy Requirement Comparison\nSmaller = More Difficult to Achieve',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xscale('log')
    ax.grid(axis='x', alpha=0.3, which='both')

    plt.tight_layout()
    plt.savefig(f'{output_dir}/02_pointing_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 02_pointing_comparison.png")


# ==============================================================================
# PLOT 3: Beam Divergence Illustration (Side View)
# ==============================================================================
def plot_beam_divergence():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    range_km = 250  # km

    # --- OPTICAL BEAM ---
    ax1.set_xlim(0, 260)
    ax1.set_ylim(-5, 5)

    # Transmitter
    ax1.add_patch(Rectangle((0, -0.05), 2, 0.1, facecolor=color_optical, edgecolor='black', linewidth=2))
    ax1.text(1, -0.7, 'Tx\n10 cm', ha='center', fontsize=10, fontweight='bold')

    # Beam (to first null - 18.9 μrad)
    beam_angle_null = 18.9e-6  # radians
    spot_radius_null = range_km * 1000 * beam_angle_null  # meters

    # Beam (half-power - 8.0 μrad)
    beam_angle_hp = 8.0e-6  # radians
    spot_radius_hp = range_km * 1000 * beam_angle_hp  # meters

    # Draw beam to first null (outer cone)
    x_beam = [2, range_km]
    y_beam_top_null = [0.05, spot_radius_null]
    y_beam_bot_null = [-0.05, -spot_radius_null]
    ax1.plot(x_beam, y_beam_top_null, color=color_optical, linewidth=1.5, linestyle='--', alpha=0.5)
    ax1.plot(x_beam, y_beam_bot_null, color=color_optical, linewidth=1.5, linestyle='--', alpha=0.5)
    ax1.fill_between(x_beam, y_beam_bot_null, y_beam_top_null, color=color_optical, alpha=0.1)

    # Draw beam half-power (inner cone)
    y_beam_top_hp = [0.05, spot_radius_hp]
    y_beam_bot_hp = [-0.05, -spot_radius_hp]
    ax1.plot(x_beam, y_beam_top_hp, color=color_optical, linewidth=2, linestyle='-')
    ax1.plot(x_beam, y_beam_bot_hp, color=color_optical, linewidth=2, linestyle='-')
    ax1.fill_between(x_beam, y_beam_bot_hp, y_beam_top_hp, color=color_optical, alpha=0.3)

    # Receiver
    ax1.add_patch(Rectangle((range_km-2, -0.05), 2, 0.1, facecolor=color_optical, edgecolor='black', linewidth=2))
    ax1.text(range_km-1, -0.7, 'Rx\n10 cm', ha='center', fontsize=10, fontweight='bold')

    # Annotations
    ax1.text(range_km + 5, spot_radius_hp, f'Half-power spot:\n{spot_radius_hp:.1f} m diameter\n(8.0 μrad)',
             va='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    ax1.text(range_km + 5, spot_radius_null, f'First null:\n{spot_radius_null:.1f} m diameter\n(18.9 μrad)',
             va='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    ax1.set_title('OPTICAL BEAM (Laser at 1550 nm)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Range (km)', fontsize=11)
    ax1.set_ylabel('Beam Radius (m)', fontsize=11)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')

    # --- RF BEAM ---
    ax2.set_xlim(0, 260)
    ax2.set_ylim(-6000, 6000)

    # Transmitter
    ax2.add_patch(Rectangle((0, -0.15), 2, 0.3, facecolor=color_rf, edgecolor='black', linewidth=2))
    ax2.text(1, -1500, 'Tx\n30 cm', ha='center', fontsize=10, fontweight='bold')

    # Beam (3 dB beamwidth = 2.19 degrees)
    beam_angle_rf = np.radians(2.19)  # radians
    spot_radius_rf = range_km * 1000 * np.tan(beam_angle_rf / 2)  # meters

    # Draw beam
    y_beam_top_rf = [0.15, spot_radius_rf]
    y_beam_bot_rf = [-0.15, -spot_radius_rf]
    ax2.plot(x_beam, y_beam_top_rf, color=color_rf, linewidth=2)
    ax2.plot(x_beam, y_beam_bot_rf, color=color_rf, linewidth=2)
    ax2.fill_between(x_beam, y_beam_bot_rf, y_beam_top_rf, color=color_rf, alpha=0.3)

    # Receiver
    ax2.add_patch(Rectangle((range_km-2, -0.15), 2, 0.3, facecolor=color_rf, edgecolor='black', linewidth=2))
    ax2.text(range_km-1, -1500, 'Rx\n30 cm', ha='center', fontsize=10, fontweight='bold')

    # Annotations
    ax2.text(range_km + 5, spot_radius_rf/2, f'3 dB beamwidth:\n{spot_radius_rf:.0f} m diameter\n(2.19°)',
             va='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    ax2.set_title('RF BEAM (Ka-band at 32 GHz)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Range (km)', fontsize=11)
    ax2.set_ylabel('Beam Radius (m)', fontsize=11)
    ax2.grid(True, alpha=0.3)

    plt.suptitle('Beam Divergence Comparison at 250 km Range\n(Not to scale vertically)',
                 fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/03_beam_divergence.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 03_beam_divergence.png")


# ==============================================================================
# PLOT 4: Data Rate Scalability
# ==============================================================================
def plot_data_rate_scalability():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Data rates from 0.1 to 100 Gbps
    data_rates = np.logspace(-1, 2, 100)  # 0.1 to 100 Gbps

    # Optical margin calculation
    # Base margin: 25.66 dB at 1 Gbps
    # Every 10× increase in data rate costs 10 dB
    optical_margin_base = 25.66
    optical_margins = optical_margin_base - 10 * np.log10(data_rates / 1.0)

    # RF margin calculation
    # Base margin: 2.8 dB at 1 Gbps
    rf_margin_base = 2.8
    rf_margins = rf_margin_base - 10 * np.log10(data_rates / 1.0)

    # Plot
    ax.plot(data_rates, optical_margins, color=color_optical, linewidth=3, label='Optical (Laser)')
    ax.plot(data_rates, rf_margins, color=color_rf, linewidth=3, label='RF (Ka-band)')

    # Add threshold line
    ax.axhline(y=3, color=color_threshold, linestyle='--', linewidth=2, label='Minimum Required (3 dB)')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1, alpha=0.5)

    # Shade regions
    ax.fill_between(data_rates, 3, 50, color='green', alpha=0.1, label='Adequate margin (>3 dB)')
    ax.fill_between(data_rates, -10, 0, color='red', alpha=0.1, label='Link fails (<0 dB)')

    # Add annotations
    ax.annotate('Optical: 10 Gbps @ 15.7 dB margin', xy=(10, 15.66), xytext=(20, 20),
                arrowprops=dict(arrowstyle='->', color=color_optical, lw=2),
                fontsize=10, fontweight='bold', color=color_optical,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.annotate('RF: fails at 1.9 Gbps', xy=(1.9, 0), xytext=(5, -5),
                arrowprops=dict(arrowstyle='->', color=color_rf, lw=2),
                fontsize=10, fontweight='bold', color=color_rf,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.set_xlabel('Data Rate (Gbps)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Link Margin (dB)', fontsize=13, fontweight='bold')
    ax.set_title('Data Rate Scalability: Link Margin vs Data Rate\n250 km Range, Same Hardware',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xscale('log')
    ax.set_xlim(0.1, 100)
    ax.set_ylim(-10, 30)
    ax.grid(True, alpha=0.3, which='both')
    ax.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/04_data_rate_scalability.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 04_data_rate_scalability.png")


# ==============================================================================
# PLOT 5: Range Sensitivity
# ==============================================================================
def plot_range_sensitivity():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Ranges from 100 to 1000 km
    ranges = np.linspace(100, 1000, 100)

    # Optical margin calculation
    # Free space loss scales as R^2 → 20*log10(R2/R1) change in dB
    # Base margin: 25.66 dB at 250 km
    optical_margin_base = 25.66
    base_range = 250
    optical_margins = optical_margin_base - 20 * np.log10(ranges / base_range)

    # RF margin calculation
    # Base margin: 2.8 dB at 250 km
    rf_margin_base = 2.8
    rf_margins = rf_margin_base - 20 * np.log10(ranges / base_range)

    # Plot
    ax.plot(ranges, optical_margins, color=color_optical, linewidth=3, label='Optical (Laser)')
    ax.plot(ranges, rf_margins, color=color_rf, linewidth=3, label='RF (Ka-band)')

    # Add threshold lines
    ax.axhline(y=3, color=color_threshold, linestyle='--', linewidth=2, label='Minimum Required (3 dB)')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1, alpha=0.5, label='Link Failure (0 dB)')
    ax.axvline(x=250, color='green', linestyle=':', linewidth=2, alpha=0.7, label='Design Range (250 km)')

    # Shade regions
    ax.fill_between(ranges, 3, 50, color='green', alpha=0.1)
    ax.fill_between(ranges, -20, 0, color='red', alpha=0.1)

    # Find where RF fails (margin = 0)
    rf_fail_range = base_range * 10**(rf_margin_base / 20)
    ax.annotate(f'RF fails at {rf_fail_range:.0f} km', xy=(rf_fail_range, 0), xytext=(rf_fail_range + 100, -5),
                arrowprops=dict(arrowstyle='->', color=color_rf, lw=2),
                fontsize=10, fontweight='bold', color=color_rf,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Optical at 500 km
    optical_500 = optical_margin_base - 20 * np.log10(500 / base_range)
    ax.annotate(f'Optical: {optical_500:.1f} dB @ 500 km', xy=(500, optical_500), xytext=(600, optical_500 + 3),
                arrowprops=dict(arrowstyle='->', color=color_optical, lw=2),
                fontsize=10, fontweight='bold', color=color_optical,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.set_xlabel('Range (km)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Link Margin (dB)', fontsize=13, fontweight='bold')
    ax.set_title('Range Sensitivity: Link Margin vs Distance\n1 Gbps Data Rate, Same Hardware',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(100, 1000)
    ax.set_ylim(-20, 30)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{output_dir}/05_range_sensitivity.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 05_range_sensitivity.png")


# ==============================================================================
# PLOT 6: Size Comparison
# ==============================================================================
def plot_size_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # --- OPTICAL ---
    ax1.set_xlim(-10, 10)
    ax1.set_ylim(-10, 10)
    ax1.set_aspect('equal')

    # 10 cm aperture (radius = 5 cm)
    circle_optical = Circle((0, 0), 5, facecolor=color_optical, edgecolor='black', linewidth=3, alpha=0.6)
    ax1.add_patch(circle_optical)

    # Add dimension lines
    ax1.plot([-5, 5], [6, 6], 'k-', linewidth=1.5)
    ax1.plot([-5, -5], [5.5, 6.5], 'k-', linewidth=1.5)
    ax1.plot([5, 5], [5.5, 6.5], 'k-', linewidth=1.5)
    ax1.text(0, 7.5, '10 cm', ha='center', fontsize=14, fontweight='bold')

    # Add specs
    ax1.text(0, -8, 'Mass: ~2.2 kg\nPower: ~4 W\nFits: 1U CubeSat',
             ha='center', fontsize=11,
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    ax1.set_title('OPTICAL TELESCOPE\n(Transmit & Receive)', fontsize=13, fontweight='bold')
    ax1.axis('off')

    # --- RF ---
    ax2.set_xlim(-20, 20)
    ax2.set_ylim(-20, 20)
    ax2.set_aspect('equal')

    # 30 cm aperture (radius = 15 cm)
    circle_rf = Circle((0, 0), 15, facecolor=color_rf, edgecolor='black', linewidth=3, alpha=0.6)
    ax2.add_patch(circle_rf)

    # Add mesh pattern to indicate deployable antenna
    for r in np.linspace(3, 15, 5):
        circle_mesh = Circle((0, 0), r, fill=False, edgecolor='white', linewidth=0.5, alpha=0.5)
        ax2.add_patch(circle_mesh)

    # Add dimension lines
    ax2.plot([-15, 15], [17, 17], 'k-', linewidth=1.5)
    ax2.plot([-15, -15], [16, 18], 'k-', linewidth=1.5)
    ax2.plot([15, 15], [16, 18], 'k-', linewidth=1.5)
    ax2.text(0, 19, '30 cm', ha='center', fontsize=14, fontweight='bold')

    # Add specs
    ax2.text(0, -17, 'Mass: ~4.1 kg\nPower: ~6 W\nNeeds: Deployment',
             ha='center', fontsize=11,
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

    ax2.set_title('RF ANTENNA\n(Transmit & Receive)', fontsize=13, fontweight='bold')
    ax2.axis('off')

    plt.suptitle('Physical Size Comparison: Aperture Diameters\nOptical is 3× smaller, 47% lighter',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/06_size_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 06_size_comparison.png")


# ==============================================================================
# PLOT 7: Trade Space Plot
# ==============================================================================
def plot_trade_space():
    fig, ax = plt.subplots(figsize=(10, 8))

    # Data points
    # X-axis: Pointing Difficulty (microradians, log scale)
    # Y-axis: Link Margin (dB)

    optical_pointing = 8.0
    optical_margin = 25.66

    rf_pointing = 38200.0
    rf_margin = 2.8

    # Plot points
    ax.scatter(optical_pointing, optical_margin, s=500, color=color_optical,
               edgecolor='black', linewidth=3, zorder=5, label='Optical (Laser)', marker='o')
    ax.scatter(rf_pointing, rf_margin, s=500, color=color_rf,
               edgecolor='black', linewidth=3, zorder=5, label='RF (Ka-band)', marker='s')

    # Add labels
    ax.text(optical_pointing * 0.6, optical_margin + 2, 'OPTICAL\nHigh margin\nHard pointing',
            ha='right', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=color_optical, alpha=0.3))

    ax.text(rf_pointing * 1.2, rf_margin - 2, 'RF\nLow margin\nEasy pointing',
            ha='left', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=color_rf, alpha=0.3))

    # Add threshold line
    ax.axhline(y=3, color=color_threshold, linestyle='--', linewidth=2,
               label='Minimum Margin (3 dB)', zorder=1)

    # Shade regions
    ax.fill_between([1, 1e6], 3, 50, color='green', alpha=0.1, label='Adequate Margin')
    ax.fill_between([1, 1e6], -10, 3, color='red', alpha=0.1, label='Insufficient Margin')

    # Add "ideal" region annotation
    ax.text(5, 20, 'IDEAL:\nEasy pointing\n+ High margin',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    # Add "poor" region annotation
    ax.text(50000, 1, 'POOR:\nHard pointing\n+ Low margin',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))

    ax.set_xlabel('Pointing Requirement (microradians, log scale)\n← Harder to achieve    Easier to achieve →',
                  fontsize=12, fontweight='bold')
    ax.set_ylabel('Link Margin (dB)\n← Less robust    More robust →',
                  fontsize=12, fontweight='bold')
    ax.set_title('Trade Space: Link Margin vs Pointing Difficulty\nThe Fundamental Trade-Off',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xscale('log')
    ax.set_xlim(1, 1e6)
    ax.set_ylim(-5, 30)
    ax.grid(True, alpha=0.3, which='both')
    ax.legend(loc='upper left', fontsize=10)

    # Invert x-axis so easier pointing is on the right
    ax.invert_xaxis()

    plt.tight_layout()
    plt.savefig(f'{output_dir}/07_trade_space.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 07_trade_space.png")


# ==============================================================================
# PLOT 8: Summary Scorecard
# ==============================================================================
def plot_summary_scorecard():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')

    # Parameters
    parameters = [
        'Aperture Size',
        'Transmit Power',
        'Data Rate',
        'Link Margin',
        'Pointing'
    ]

    optical_values = [
        '10 cm',
        '0.122 W',
        '10+ Gbps',
        '25.66 dB',
        '8.0 μrad'
    ]

    rf_values = [
        '30 cm',
        '1.2 W',
        '~2 Gbps max',
        '2.8 dB',
        '2.19° (38,200 μrad)'
    ]

    winners = [
        'Optical',
        'Optical',
        'Optical',
        'Optical',
        'RF'
    ]

    # Create table
    cell_height = 0.12
    cell_width_param = 0.25
    cell_width_value = 0.3
    cell_width_winner = 0.15

    # Header
    y_pos = 0.95
    ax.text(0.125, y_pos, 'Parameter', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(0.375, y_pos, 'Optical (Laser)', ha='center', va='center', fontsize=14, fontweight='bold', color=color_optical)
    ax.text(0.675, y_pos, 'RF (Ka-band)', ha='center', va='center', fontsize=14, fontweight='bold', color=color_rf)
    ax.text(0.925, y_pos, 'Winner', ha='center', va='center', fontsize=14, fontweight='bold')

    # Draw header line
    ax.plot([0, 1], [y_pos - 0.04, y_pos - 0.04], 'k-', linewidth=2)

    # Rows
    y_pos = 0.85
    for i, (param, opt_val, rf_val, winner) in enumerate(zip(parameters, optical_values, rf_values, winners)):
        # Parameter name
        ax.text(0.125, y_pos, param, ha='center', va='center', fontsize=12, fontweight='bold')

        # Optical value
        bg_color_opt = color_good if winner == 'Optical' else 'white'
        rect_opt = FancyBboxPatch((0.225, y_pos - 0.04), 0.3, 0.08,
                                   boxstyle="round,pad=0.01",
                                   facecolor=bg_color_opt, edgecolor='black',
                                   linewidth=1.5, alpha=0.3 if winner != 'Optical' else 0.5)
        ax.add_patch(rect_opt)
        ax.text(0.375, y_pos, opt_val, ha='center', va='center', fontsize=11)

        # RF value
        bg_color_rf = color_good if winner == 'RF' else 'white'
        rect_rf = FancyBboxPatch((0.525, y_pos - 0.04), 0.3, 0.08,
                                  boxstyle="round,pad=0.01",
                                  facecolor=bg_color_rf, edgecolor='black',
                                  linewidth=1.5, alpha=0.3 if winner != 'RF' else 0.5)
        ax.add_patch(rect_rf)
        ax.text(0.675, y_pos, rf_val, ha='center', va='center', fontsize=11)

        # Winner
        winner_color = color_optical if winner == 'Optical' else color_rf
        ax.text(0.925, y_pos, f'✓ {winner}', ha='center', va='center',
                fontsize=11, fontweight='bold', color=winner_color)

        y_pos -= 0.15

    # Overall recommendation box
    y_pos -= 0.05
    ax.plot([0, 1], [y_pos, y_pos], 'k-', linewidth=2)
    y_pos -= 0.1

    rect_rec = FancyBboxPatch((0.1, y_pos - 0.06), 0.8, 0.12,
                               boxstyle="round,pad=0.02",
                               facecolor='lightgreen', edgecolor='black',
                               linewidth=3, alpha=0.6)
    ax.add_patch(rect_rec)
    ax.text(0.5, y_pos, 'RECOMMENDATION: OPTICAL (LASER) CROSSLINKS',
            ha='center', va='center', fontsize=14, fontweight='bold')

    # Rationale
    y_pos -= 0.15
    rationale = ('Optical wins 4/5 parameters with decisive advantages:\n'
                 '• 9× better link margin (25.66 vs 2.8 dB) = far more robust system\n'
                 '• 5× higher data rate scalability (10+ Gbps vs ~2 Gbps)\n'
                 '• 47% lighter (2.2 vs 4.1 kg) and 10× lower power\n'
                 '• Pointing challenge (4,800× harder) is manageable with FSM technology')
    ax.text(0.5, y_pos, rationale, ha='center', va='top', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.suptitle('CROSSLINK TRADE STUDY SUMMARY SCORECARD\n250 km Range, 1 Gbps Data Rate, Small Satellites',
                 fontsize=15, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/08_summary_scorecard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 08_summary_scorecard.png")


# ==============================================================================
# PLOT 9: Airy Disk Pattern (Bonus)
# ==============================================================================
def plot_airy_disk():
    try:
        from scipy.special import j1
    except ImportError:
        print("⚠ Skipping Airy disk plot (scipy not installed)")
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Radial coordinate (in units of beam divergence)
    theta = np.linspace(0, 30, 1000)  # microradians

    # Airy pattern intensity: I(θ) = I0 * [2*J1(x)/x]^2
    # where x = π * D * sin(θ) / λ
    # For small angles: sin(θ) ≈ θ

    # Normalize to beam divergence units
    # First null at 1.22 λ/D = 18.9 μrad
    # Half-power at 0.514 λ/D = 8.0 μrad

    x = theta / 18.9 * 1.22 * np.pi  # Convert to Bessel argument
    x[0] = 1e-10  # Avoid division by zero
    intensity = (2 * j1(x) / x) ** 2

    # Plot 1: Intensity vs angle
    ax1.plot(theta, intensity, color=color_optical, linewidth=2.5)
    ax1.fill_between(theta, 0, intensity, color=color_optical, alpha=0.3)

    # Mark key points
    ax1.axvline(x=8.0, color='red', linestyle='--', linewidth=2, label='Half-power (8.0 μrad)')
    ax1.axhline(y=0.5, color='red', linestyle=':', linewidth=1.5, alpha=0.7)
    ax1.axvline(x=18.9, color='orange', linestyle='--', linewidth=2, label='First null (18.9 μrad)')

    ax1.set_xlabel('Angular Distance from Center (microradians)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Relative Intensity', fontsize=12, fontweight='bold')
    ax1.set_title('Airy Disk Intensity Profile\nOptical Beam Pattern', fontsize=13, fontweight='bold')
    ax1.set_xlim(0, 30)
    ax1.set_ylim(0, 1.1)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=10)

    # Annotations
    ax1.annotate('Pointing requirement\n(half-power beamwidth)',
                 xy=(8, 0.5), xytext=(12, 0.7),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2),
                 fontsize=10, fontweight='bold', color='red')

    ax1.annotate('Beam divergence\n(to first null)',
                 xy=(18.9, 0), xytext=(20, 0.2),
                 arrowprops=dict(arrowstyle='->', color='orange', lw=2),
                 fontsize=10, fontweight='bold', color='orange')

    # Plot 2: 2D intensity pattern
    x_2d = np.linspace(-30, 30, 500)
    y_2d = np.linspace(-30, 30, 500)
    X, Y = np.meshgrid(x_2d, y_2d)
    R = np.sqrt(X**2 + Y**2)

    x_bessel = R / 18.9 * 1.22 * np.pi
    x_bessel[x_bessel == 0] = 1e-10
    intensity_2d = (2 * j1(x_bessel) / x_bessel) ** 2

    im = ax2.contourf(X, Y, intensity_2d, levels=20, cmap='hot')

    # Add circles for reference
    circle_hp = Circle((0, 0), 8.0, fill=False, edgecolor='cyan', linewidth=2, linestyle='--', label='Half-power (8 μrad)')
    circle_null = Circle((0, 0), 18.9, fill=False, edgecolor='lime', linewidth=2, linestyle='--', label='First null (18.9 μrad)')
    ax2.add_patch(circle_hp)
    ax2.add_patch(circle_null)

    ax2.set_xlabel('X Position (microradians)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Y Position (microradians)', fontsize=12, fontweight='bold')
    ax2.set_title('Airy Disk 2D Pattern\nBeam Intensity at Receiver', fontsize=13, fontweight='bold')
    ax2.set_aspect('equal')
    ax2.legend(fontsize=9)

    plt.colorbar(im, ax=ax2, label='Relative Intensity')

    plt.suptitle('Optical Beam Diffraction Pattern (Airy Disk)\nWhy Pointing Requirement is 8 μrad, Not 18.9 μrad',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/09_airy_disk_pattern.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated: 09_airy_disk_pattern.png")


# ==============================================================================
# MAIN: Generate all plots
# ==============================================================================
def main():
    print("\n" + "="*60)
    print("Generating plots for Optical vs RF Crosslink Trade Study")
    print("="*60 + "\n")

    plot_link_margin_comparison()
    plot_pointing_comparison()
    plot_beam_divergence()
    plot_data_rate_scalability()
    plot_range_sensitivity()
    plot_size_comparison()
    plot_trade_space()
    plot_summary_scorecard()
    plot_airy_disk()

    print("\n" + "="*60)
    print(f"✓ Plots generated successfully!")
    print(f"✓ Output directory: {output_dir}/")
    print("="*60 + "\n")

    print("Plot descriptions:")
    print("  01 - Link Margin Comparison (bar chart)")
    print("  02 - Pointing Comparison (horizontal bar, log scale)")
    print("  03 - Beam Divergence Illustration (side view)")
    print("  04 - Data Rate Scalability (margin vs data rate)")
    print("  05 - Range Sensitivity (margin vs distance)")
    print("  06 - Size Comparison (physical apertures)")
    print("  07 - Trade Space Plot (margin vs pointing difficulty)")
    print("  08 - Summary Scorecard (decision table)")
    print("  09 - Airy Disk Pattern (diffraction explanation)")
    print()


if __name__ == "__main__":
    main()
