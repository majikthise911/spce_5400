"""
Generate visualizations for Optical vs RF Crosslink Trade Study
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Wedge
import matplotlib.colors as mcolors

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
colors = {'optical': '#2E86AB', 'rf': '#A23B72'}

# Create output directory path
output_dir = 'outputs/'

# ============================================================================
# 1. LINK MARGIN COMPARISON BAR CHART
# ============================================================================
def create_link_margin_comparison():
    fig, ax = plt.subplots(figsize=(10, 6))

    technologies = ['Optical\n(Laser)', 'RF\n(Ka-band)']
    margins = [25.66, 2.88]
    colors_list = [colors['optical'], colors['rf']]

    bars = ax.bar(technologies, margins, color=colors_list, alpha=0.8, edgecolor='black', linewidth=2)

    # Add value labels on bars
    for bar, margin in zip(bars, margins):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{margin:.2f} dB',
                ha='center', va='bottom', fontsize=14, fontweight='bold')

    # Add minimum requirement line
    ax.axhline(y=3, color='red', linestyle='--', linewidth=2, label='Minimum Requirement (3 dB)')

    # Add ratio annotation
    ax.text(0.5, 20, 'Optical has 8.9× more margin',
            ha='center', fontsize=12, style='italic',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    ax.set_ylabel('Link Margin (dB)', fontsize=14, fontweight='bold')
    ax.set_title('Link Margin Comparison: Optical vs RF\n250 km separation, 1 Gbps data rate',
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_ylim(0, 30)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir + '1_link_margin_comparison.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: 1_link_margin_comparison.png")
    plt.close()

# ============================================================================
# 2. DATA RATE SCALABILITY CHART
# ============================================================================
def create_data_rate_scalability():
    fig, ax = plt.subplots(figsize=(12, 7))

    # Data rates from 0.5 to 10 Gbps
    data_rates = np.array([0.5, 1, 2, 5, 10])

    # Optical margins (starts at 25.66 dB at 1 Gbps)
    # Each 10x increase costs 10 dB
    optical_baseline = 25.66
    optical_margins = optical_baseline - 10 * np.log10(data_rates / 1.0)

    # RF margins (starts at 2.88 dB at 1 Gbps)
    rf_baseline = 2.88
    rf_margins = rf_baseline - 10 * np.log10(data_rates / 1.0)

    # Plot lines
    ax.plot(data_rates, optical_margins, 'o-', linewidth=3, markersize=10,
            color=colors['optical'], label='Optical (Laser)')
    ax.plot(data_rates, rf_margins, 's-', linewidth=3, markersize=10,
            color=colors['rf'], label='RF (Ka-band)')

    # Add minimum requirement line
    ax.axhline(y=3, color='red', linestyle='--', linewidth=2, label='Minimum Requirement (3 dB)')
    ax.axhline(y=0, color='black', linestyle=':', linewidth=1, alpha=0.5)

    # Shade "link fails" region
    ax.fill_between(data_rates, -10, 0, alpha=0.2, color='red', label='Link Fails (margin < 0)')

    # Add annotations
    ax.annotate('Optical: 15.66 dB @ 10 Gbps\n(still excellent)',
                xy=(10, optical_margins[-1]), xytext=(8, 18),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['optical']),
                fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    ax.annotate('RF fails @ 2 Gbps\n(margin < 0)',
                xy=(2, rf_margins[2]), xytext=(3.5, -3),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['rf']),
                fontsize=11, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    ax.set_xlabel('Data Rate (Gbps)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Link Margin (dB)', fontsize=14, fontweight='bold')
    ax.set_title('Data Rate Scalability: Optical vs RF\nHow margin degrades with increasing data rate',
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlim(0, 11)
    ax.set_ylim(-10, 30)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir + '2_data_rate_scalability.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: 2_data_rate_scalability.png")
    plt.close()

# ============================================================================
# 3. RANGE SENSITIVITY CHART
# ============================================================================
def create_range_sensitivity():
    fig, ax = plt.subplots(figsize=(12, 7))

    # Ranges from 100 to 600 km
    ranges = np.array([100, 150, 200, 250, 300, 400, 500, 600])

    # Optical margins (baseline 25.66 dB at 250 km)
    # Path loss scales as 20*log10(R)
    optical_baseline = 25.66
    optical_margins = optical_baseline - 20 * np.log10(ranges / 250.0)

    # RF margins (baseline 2.88 dB at 250 km)
    rf_baseline = 2.88
    rf_margins = rf_baseline - 20 * np.log10(ranges / 250.0)

    # Plot lines
    ax.plot(ranges, optical_margins, 'o-', linewidth=3, markersize=10,
            color=colors['optical'], label='Optical (Laser)')
    ax.plot(ranges, rf_margins, 's-', linewidth=3, markersize=10,
            color=colors['rf'], label='RF (Ka-band)')

    # Add minimum requirement line
    ax.axhline(y=3, color='red', linestyle='--', linewidth=2, label='Minimum Requirement (3 dB)')
    ax.axhline(y=0, color='black', linestyle=':', linewidth=1, alpha=0.5)

    # Shade "link fails" region
    ax.fill_between(ranges, -10, 0, alpha=0.2, color='red', label='Link Fails (margin < 0)')

    # Add baseline marker
    ax.axvline(x=250, color='green', linestyle=':', linewidth=2, alpha=0.5, label='Baseline (250 km)')

    # Add annotations
    ax.annotate('Optical: 19.62 dB @ 500 km\n(still robust)',
                xy=(500, optical_margins[6]), xytext=(450, 25),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['optical']),
                fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    ax.annotate('RF fails @ 500 km\n(-3.12 dB)',
                xy=(500, rf_margins[6]), xytext=(400, -5),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['rf']),
                fontsize=11, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    ax.set_xlabel('Inter-Satellite Distance (km)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Link Margin (dB)', fontsize=14, fontweight='bold')
    ax.set_title('Range Sensitivity: Optical vs RF\nHow margin changes with satellite separation',
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlim(80, 620)
    ax.set_ylim(-10, 35)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir + '3_range_sensitivity.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: 3_range_sensitivity.png")
    plt.close()

# ============================================================================
# 4. FIVE-PARAMETER RADAR CHART
# ============================================================================
def create_radar_chart():
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

    # Categories (5 parameters from assignment)
    categories = ['Link Margin\n(higher better)',
                  'Aperture Size\n(smaller better)',
                  'Power\n(lower better)',
                  'Data Rate\n(higher better)',
                  'Pointing\n(easier better)']

    # Normalize scores to 0-10 scale for visualization
    # Optical scores
    optical_scores = [
        10,  # Link margin: 25.66 dB (excellent)
        10,  # Aperture: 10 cm (3x smaller than RF)
        10,  # Power: 0.122W (10x less than RF)
        10,  # Data rate: 10+ Gbps scalable
        3    # Pointing: 18.9 urad (very challenging)
    ]

    # RF scores
    rf_scores = [
        3,   # Link margin: 2.88 dB (minimal)
        3,   # Aperture: 30 cm (3x larger)
        1,   # Power: 1.2W (10x more)
        4,   # Data rate: ~2 Gbps max
        10   # Pointing: 2.183° (very easy)
    ]

    # Number of variables
    N = len(categories)

    # Compute angle for each axis
    angles = [n / float(N) * 2 * np.pi for n in range(N)]

    # Close the plot
    optical_scores += optical_scores[:1]
    rf_scores += rf_scores[:1]
    angles += angles[:1]

    # Plot
    ax.plot(angles, optical_scores, 'o-', linewidth=3, markersize=8,
            color=colors['optical'], label='Optical (Laser)')
    ax.fill(angles, optical_scores, alpha=0.25, color=colors['optical'])

    ax.plot(angles, rf_scores, 's-', linewidth=3, markersize=8,
            color=colors['rf'], label='RF (Ka-band)')
    ax.fill(angles, rf_scores, alpha=0.25, color=colors['rf'])

    # Fix axis to go in the right order and start at 12 o'clock
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Draw axis lines for each angle and label
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)

    # Set radial limits and labels
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=10)
    ax.set_rlabel_position(180)

    # Add legend
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)

    # Add title
    plt.title('Five-Parameter Comparison: Optical vs RF\nOptical wins 4 of 5 categories',
              fontsize=16, fontweight='bold', pad=30)

    plt.tight_layout()
    plt.savefig(output_dir + '4_radar_chart.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: 4_radar_chart.png")
    plt.close()

# ============================================================================
# 5. SWaP COMPARISON
# ============================================================================
def create_swap_comparison():
    fig, axes = plt.subplots(1, 3, figsize=(15, 6))

    # Data
    categories = ['Optical\n(Laser)', 'RF\n(Ka-band)']

    # Aperture size (cm)
    apertures = [10, 30]
    axes[0].bar(categories, apertures, color=[colors['optical'], colors['rf']],
                alpha=0.8, edgecolor='black', linewidth=2)
    axes[0].set_ylabel('Aperture Diameter (cm)', fontsize=12, fontweight='bold')
    axes[0].set_title('Aperture Size\n(smaller is better)', fontsize=13, fontweight='bold')
    axes[0].set_ylim(0, 35)
    for i, v in enumerate(apertures):
        axes[0].text(i, v + 1, f'{v} cm', ha='center', fontsize=12, fontweight='bold')
    axes[0].text(0.5, 25, '3× smaller', ha='center', fontsize=11, style='italic',
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5),
                 transform=axes[0].transData)

    # Mass (kg)
    masses = [2.2, 4.2]
    axes[1].bar(categories, masses, color=[colors['optical'], colors['rf']],
                alpha=0.8, edgecolor='black', linewidth=2)
    axes[1].set_ylabel('Payload Mass (kg)', fontsize=12, fontweight='bold')
    axes[1].set_title('Mass\n(lighter is better)', fontsize=13, fontweight='bold')
    axes[1].set_ylim(0, 5)
    for i, v in enumerate(masses):
        axes[1].text(i, v + 0.1, f'{v} kg', ha='center', fontsize=12, fontweight='bold')
    axes[1].text(0.5, 3.5, '2 kg lighter', ha='center', fontsize=11, style='italic',
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5),
                 transform=axes[1].transData)

    # Power (W)
    powers = [0.122, 1.2]
    axes[2].bar(categories, powers, color=[colors['optical'], colors['rf']],
                alpha=0.8, edgecolor='black', linewidth=2)
    axes[2].set_ylabel('Transmit Power (W)', fontsize=12, fontweight='bold')
    axes[2].set_title('Power\n(lower is better)', fontsize=13, fontweight='bold')
    axes[2].set_ylim(0, 1.5)
    for i, v in enumerate(powers):
        axes[2].text(i, v + 0.05, f'{v} W', ha='center', fontsize=12, fontweight='bold')
    axes[2].text(0.5, 1.0, '10× lower', ha='center', fontsize=11, style='italic',
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5),
                 transform=axes[2].transData)

    for ax in axes:
        ax.grid(axis='y', alpha=0.3)

    fig.suptitle('SWaP Comparison: Optical vs RF\nSize, Weight, and Power',
                 fontsize=16, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(output_dir + '5_swap_comparison.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: 5_swap_comparison.png")
    plt.close()

# ============================================================================
# 6. BEAM DIVERGENCE ILLUSTRATION
# ============================================================================
def create_beam_divergence():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

    # Common parameters
    range_km = 250
    sat_size = 0.5  # Satellite size in plot units

    # -------------------------
    # Optical beam (top)
    # -------------------------
    divergence_optical = 18.9e-6  # radians
    spot_diameter_optical = divergence_optical * range_km * 1000  # in meters

    # Scale for visualization (exaggerate angle for visibility)
    scale_factor = 5000
    half_angle_optical = divergence_optical * scale_factor

    # Draw satellite
    sat1 = patches.Rectangle((0, -sat_size/2), sat_size, sat_size,
                             facecolor='gray', edgecolor='black', linewidth=2)
    ax1.add_patch(sat1)
    ax1.text(0.25, 0, 'Sat A', ha='center', va='center', fontsize=10, fontweight='bold')

    # Draw narrow beam cone (exaggerated for visibility)
    beam_end = range_km
    beam_width = beam_end * half_angle_optical
    beam = patches.Polygon([[sat_size, 0],
                           [beam_end, beam_width],
                           [beam_end, -beam_width]],
                          facecolor=colors['optical'], alpha=0.3,
                          edgecolor=colors['optical'], linewidth=2)
    ax1.add_patch(beam)

    # Draw receiving satellite
    sat2 = patches.Rectangle((beam_end, -sat_size/2), sat_size, sat_size,
                             facecolor='gray', edgecolor='black', linewidth=2)
    ax1.add_patch(sat2)
    ax1.text(beam_end + 0.25, 0, 'Sat B', ha='center', va='center', fontsize=10, fontweight='bold')

    # Draw spot size circle
    spot_circle = patches.Circle((beam_end + sat_size/2, 0), beam_width,
                                facecolor='none', edgecolor='red',
                                linewidth=2, linestyle='--')
    ax1.add_patch(spot_circle)

    # Annotations
    ax1.annotate('', xy=(beam_end, 0), xytext=(sat_size, 0),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax1.text(beam_end/2, -15, '250 km', ha='center', fontsize=11, fontweight='bold')

    ax1.text(beam_end + sat_size/2, beam_width + 5,
            f'Spot: {spot_diameter_optical:.1f} m diameter',
            ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    ax1.text(beam_end/2, beam_width + 8,
            'Divergence: 18.9 microradians\n(0.0011 degrees)',
            ha='center', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

    ax1.text(5, 18, 'OPTICAL (LASER) BEAM', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='black', linewidth=2))

    ax1.set_xlim(-5, beam_end + 10)
    ax1.set_ylim(-25, 25)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Optical: Very Narrow Beam = Precise Pointing Required',
                 fontsize=13, fontweight='bold', pad=10)

    # -------------------------
    # RF beam (bottom)
    # -------------------------
    beamwidth_rf = 2.183  # degrees
    half_angle_rf = np.radians(beamwidth_rf / 2)

    # Draw satellite
    sat3 = patches.Rectangle((0, -sat_size/2), sat_size, sat_size,
                             facecolor='gray', edgecolor='black', linewidth=2)
    ax2.add_patch(sat3)
    ax2.text(0.25, 0, 'Sat A', ha='center', va='center', fontsize=10, fontweight='bold')

    # Draw wide beam cone
    beam_end = range_km
    beam_width_rf = beam_end * half_angle_rf
    beam2 = patches.Polygon([[sat_size, 0],
                            [beam_end, beam_width_rf],
                            [beam_end, -beam_width_rf]],
                           facecolor=colors['rf'], alpha=0.3,
                           edgecolor=colors['rf'], linewidth=2)
    ax2.add_patch(beam2)

    # Draw receiving satellite
    sat4 = patches.Rectangle((beam_end, -sat_size/2), sat_size, sat_size,
                             facecolor='gray', edgecolor='black', linewidth=2)
    ax2.add_patch(sat4)
    ax2.text(beam_end + 0.25, 0, 'Sat B', ha='center', va='center', fontsize=10, fontweight='bold')

    # Draw spot size circle
    spot_circle2 = patches.Circle((beam_end + sat_size/2, 0), beam_width_rf,
                                 facecolor='none', edgecolor='red',
                                 linewidth=2, linestyle='--')
    ax2.add_patch(spot_circle2)

    # Annotations
    ax2.annotate('', xy=(beam_end, 0), xytext=(sat_size, 0),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax2.text(beam_end/2, -25, '250 km', ha='center', fontsize=11, fontweight='bold')

    spot_diameter_rf = 2 * beam_width_rf * 1000  # convert to meters
    ax2.text(beam_end + sat_size/2, beam_width_rf + 8,
            f'Spot: {spot_diameter_rf:.0f} m diameter',
            ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    ax2.text(beam_end/2, beam_width_rf - 10,
            'Beamwidth: 2.183 degrees\n(115,000× wider than optical)',
            ha='center', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    ax2.text(5, 30, 'RF (Ka-BAND) BEAM', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='black', linewidth=2))

    ax2.set_xlim(-5, beam_end + 10)
    ax2.set_ylim(-40, 40)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('RF: Very Wide Beam = Easy Pointing (body-mounted antenna OK)',
                 fontsize=13, fontweight='bold', pad=10)

    fig.suptitle('Beam Divergence Comparison: Optical vs RF\nShowing beamwidth difference at 250 km',
                fontsize=16, fontweight='bold', y=0.98)

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(output_dir + '6_beam_divergence.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: 6_beam_divergence.png")
    plt.close()

# ============================================================================
# 7. LINK BUDGET WATERFALL CHART
# ============================================================================
def create_waterfall_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # -------------------------
    # Optical waterfall
    # -------------------------
    categories_opt = ['Tx Power\n0.122W', 'Free Space\nLoss', 'Tx Gain\n(10cm)',
                     'Rx Gain\n(10cm)', 'Pointing\nLoss', 'Line\nLosses',
                     'Received\nPower', 'Required\nPower', 'MARGIN']

    values_opt = [
        10*np.log10(0.122),  # Tx power: -9.14 dBW
        -246.1,               # Free space loss
        106.1,                # Tx gain
        106.1,                # Rx gain
        -3.0,                 # Pointing loss
        -6.0,                 # Line losses
        0,                    # Received power (calculated)
        0,                    # Required power (reference)
        0                     # Margin (calculated)
    ]

    # Calculate cumulative for waterfall
    cumulative_opt = [values_opt[0]]
    for i in range(1, 6):
        cumulative_opt.append(cumulative_opt[-1] + values_opt[i])

    # Received power
    rx_power_opt = cumulative_opt[-1]
    cumulative_opt.append(rx_power_opt)

    # Required power
    req_power_opt = -77.67
    cumulative_opt.append(req_power_opt)

    # Margin
    margin_opt = rx_power_opt - req_power_opt
    cumulative_opt.append(margin_opt)

    # Plot bars
    colors_opt_bars = []
    for i, val in enumerate(values_opt[:6]):
        if val > 0:
            colors_opt_bars.append('green')
        else:
            colors_opt_bars.append('red')
    colors_opt_bars.extend(['blue', 'orange', 'purple'])

    # Create waterfall
    for i in range(len(categories_opt)):
        if i == 0:
            ax1.bar(i, cumulative_opt[i], color=colors_opt_bars[i], alpha=0.7, edgecolor='black', linewidth=1.5)
            ax1.text(i, cumulative_opt[i]/2, f'{values_opt[i]:.1f} dB',
                    ha='center', va='center', fontsize=9, fontweight='bold')
        elif i < 6:
            start = cumulative_opt[i-1]
            height = values_opt[i]
            ax1.bar(i, height, bottom=start, color=colors_opt_bars[i], alpha=0.7, edgecolor='black', linewidth=1.5)
            ax1.text(i, start + height/2, f'{values_opt[i]:.1f} dB',
                    ha='center', va='center', fontsize=9, fontweight='bold')
            # Draw connector line
            ax1.plot([i-0.4, i-0.6], [cumulative_opt[i-1], cumulative_opt[i-1]], 'k--', linewidth=1)
        elif i == 6:  # Received power
            ax1.bar(i, cumulative_opt[i], color=colors_opt_bars[i], alpha=0.7, edgecolor='black', linewidth=2)
            ax1.text(i, cumulative_opt[i]/2, f'{cumulative_opt[i]:.1f} dBW',
                    ha='center', va='center', fontsize=9, fontweight='bold', color='white')
        elif i == 7:  # Required power
            ax1.bar(i, cumulative_opt[i], color=colors_opt_bars[i], alpha=0.7, edgecolor='black', linewidth=2)
            ax1.text(i, cumulative_opt[i]/2, f'{cumulative_opt[i]:.1f} dBW',
                    ha='center', va='center', fontsize=9, fontweight='bold')
        else:  # Margin
            ax1.bar(i, cumulative_opt[i], color=colors_opt_bars[i], alpha=0.7, edgecolor='black', linewidth=3)
            ax1.text(i, cumulative_opt[i]/2, f'{cumulative_opt[i]:.1f} dB',
                    ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    ax1.set_xticks(range(len(categories_opt)))
    ax1.set_xticklabels(categories_opt, fontsize=10, rotation=0)
    ax1.set_ylabel('Power Level (dBW or dB)', fontsize=12, fontweight='bold')
    ax1.set_title('OPTICAL Link Budget Waterfall\nMargin = 25.66 dB',
                 fontsize=14, fontweight='bold', pad=15)
    ax1.axhline(y=0, color='black', linewidth=0.5, alpha=0.3)
    ax1.grid(axis='y', alpha=0.3)

    # -------------------------
    # RF waterfall
    # -------------------------
    categories_rf = ['Tx Power\n1.2W', 'Tx Gain\n(30cm)', 'Free Space\nLoss',
                    'Rx Gain\n(30cm)', 'Pointing\nLoss', 'Other\nLosses',
                    'Received\nPower', 'Noise\nFloor', 'C/N0',
                    'Required\nC/N0', 'MARGIN']

    values_rf = [
        10*np.log10(1.2),    # Tx power: 0.79 dBW
        37.8,                 # Tx gain
        -170.5,               # Free space loss
        37.8,                 # Rx gain
        -1.0,                 # Pointing loss
        -3.0,                 # Other losses
        0,                    # Received power (calculated)
        -200.5,               # Noise floor
        0,                    # C/N0 (calculated)
        99.6,                 # Required C/N0
        0                     # Margin (calculated)
    ]

    # Calculate cumulative
    cumulative_rf = [values_rf[0]]
    for i in range(1, 6):
        cumulative_rf.append(cumulative_rf[-1] + values_rf[i])

    # Received power
    rx_power_rf = cumulative_rf[-1]
    cumulative_rf.append(rx_power_rf)

    # Noise floor
    noise_rf = -200.5
    cumulative_rf.append(noise_rf)

    # C/N0
    cn0_rf = rx_power_rf - noise_rf
    cumulative_rf.append(cn0_rf)

    # Required C/N0
    req_cn0_rf = 99.6
    cumulative_rf.append(req_cn0_rf)

    # Margin
    margin_rf = cn0_rf - req_cn0_rf
    cumulative_rf.append(margin_rf)

    # Plot bars (simplified for RF)
    colors_rf_bars = []
    for i, val in enumerate(values_rf[:6]):
        if val > 0:
            colors_rf_bars.append('green')
        else:
            colors_rf_bars.append('red')
    colors_rf_bars.extend(['blue', 'orange', 'cyan', 'magenta', 'purple'])

    # Create waterfall (simplified version - just show key stages)
    stages_rf = [0.79, 38.59, -131.91, -94.11, -95.11, -98.11]  # Cumulative at each stage
    stage_labels = ['0.79', '38.6', '-132', '-94', '-95', '-98']

    for i in range(6):
        if i == 0:
            ax2.bar(i, stages_rf[i], color=colors_rf_bars[i], alpha=0.7, edgecolor='black', linewidth=1.5)
            ax2.text(i, stages_rf[i]/2, f'{values_rf[i]:.1f} dB',
                    ha='center', va='center', fontsize=9, fontweight='bold')
        else:
            start = stages_rf[i-1]
            height = values_rf[i]
            ax2.bar(i, height, bottom=start, color=colors_rf_bars[i], alpha=0.7, edgecolor='black', linewidth=1.5)
            ax2.text(i, start + height/2, f'{values_rf[i]:.1f} dB',
                    ha='center', va='center', fontsize=9, fontweight='bold')
            ax2.plot([i-0.4, i-0.6], [stages_rf[i-1], stages_rf[i-1]], 'k--', linewidth=1)

    # Received power bar
    ax2.bar(6, rx_power_rf, color='blue', alpha=0.7, edgecolor='black', linewidth=2)
    ax2.text(6, rx_power_rf/2, f'{rx_power_rf:.1f} dBW',
            ha='center', va='center', fontsize=9, fontweight='bold', color='white')

    # Skip noise floor bar, go straight to C/N0
    ax2.bar(8, cn0_rf, color='cyan', alpha=0.7, edgecolor='black', linewidth=2)
    ax2.text(8, cn0_rf/2, f'{cn0_rf:.1f} dB-Hz',
            ha='center', va='center', fontsize=9, fontweight='bold')

    # Required C/N0
    ax2.bar(9, req_cn0_rf, color='magenta', alpha=0.7, edgecolor='black', linewidth=2)
    ax2.text(9, req_cn0_rf/2, f'{req_cn0_rf:.1f} dB-Hz',
            ha='center', va='center', fontsize=9, fontweight='bold')

    # Margin (small bar)
    ax2.bar(10, margin_rf, color='purple', alpha=0.7, edgecolor='black', linewidth=3)
    ax2.text(10, margin_rf/2 if margin_rf > 5 else margin_rf + 2, f'{margin_rf:.1f} dB',
            ha='center', va='center', fontsize=11, fontweight='bold', color='white' if margin_rf > 5 else 'black')

    ax2.set_xticks(range(len(categories_rf)))
    ax2.set_xticklabels(categories_rf, fontsize=10, rotation=0)
    ax2.set_ylabel('Power Level (dBW or dB-Hz)', fontsize=12, fontweight='bold')
    ax2.set_title('RF Link Budget Waterfall\nMargin = 2.88 dB',
                 fontsize=14, fontweight='bold', pad=15)
    ax2.axhline(y=0, color='black', linewidth=0.5, alpha=0.3)
    ax2.grid(axis='y', alpha=0.3)

    fig.suptitle('Link Budget Waterfall Charts: Optical vs RF\nShowing gains and losses from transmit to final margin',
                fontsize=16, fontweight='bold', y=0.98)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_dir + '7_waterfall_charts.png', dpi=300, bbox_inches='tight')
    print("[OK] Created: 7_waterfall_charts.png")
    plt.close()

# ============================================================================
# MAIN EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("Creating visualizations for Optical vs RF Trade Study")
    print("="*60 + "\n")

    try:
        create_link_margin_comparison()
        create_data_rate_scalability()
        create_range_sensitivity()
        create_radar_chart()
        create_swap_comparison()
        create_beam_divergence()
        create_waterfall_chart()

        print("\n" + "="*60)
        print("[SUCCESS] All visualizations created successfully!")
        print("="*60)
        print(f"\nSaved to: {output_dir}")
        print("\nGenerated files:")
        print("  1. 1_link_margin_comparison.png")
        print("  2. 2_data_rate_scalability.png")
        print("  3. 3_range_sensitivity.png")
        print("  4. 4_radar_chart.png")
        print("  5. 5_swap_comparison.png")
        print("  6. 6_beam_divergence.png")
        print("  7. 7_waterfall_charts.png")

    except Exception as e:
        print(f"\n[ERROR] Error creating visualizations: {e}")
        import traceback
        traceback.print_exc()
