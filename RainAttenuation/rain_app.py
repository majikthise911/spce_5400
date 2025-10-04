"""
Rain Attenuation Calculator - Interactive GUI Application
Standalone version of rain_attenuation_notebook.ipynb using Matplotlib widgets
"""

import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button
import matplotlib.patches as mpatches
import os

# Constants for rain attenuation model from ITU-R P.618
MIN_ELEVATION = 1.0
EXP_COEFFICIENT = -0.015
REDUCTION_DENOMINATOR = 35
LAT_THRESHOLD = 23
RAIN_HEIGHT_BASE = 5
RAIN_HEIGHT_COEFF = 0.073

# Table 2.1 - Coefficients for rain attenuation model
coeff_v = {
    1.0: {'a': 0.0000308, 'b': .8592},
    1.5: {'a': 0.0000574, 'b': .8957},
    2.0: {'a': 0.0000998, 'b': .9490},
    2.5: {'a': 0.0001464, 'b': 1.0085},
    3.0: {'a': 0.0001942, 'b': 1.0688},
    3.5: {'a': 0.0002346, 'b': 1.1387},
    4.0: {'a': 0.0002461, 'b': 1.2476}
}

coeff_h = {
    1.0: {'a': 0.0000259, 'b': 0.9691},
    1.5: {'a': 0.0000443, 'b': 1.0185},
    2.0: {'a': 0.0000847, 'b': 1.0664},
    2.5: {'a': 0.0001321, 'b': 1.1209},
    3.0: {'a': 0.0001390, 'b': 1.2322},
    3.5: {'a': 0.0001155, 'b': 1.4189},
    4.0: {'a': 0.0001071, 'b': 1.6009}
}

# Table 2.5 - European city locations (with longitude added for mapping)
locations = {
    'Madrid': {'phi': 40.4, 'hs_m': 588, 'lon': -3.7},
    'Tirana': {'phi': 41.3, 'hs_m': 104, 'lon': 19.8},
    'Rome': {'phi': 41.9, 'hs_m': 14, 'lon': 12.5},
    'Pristina': {'phi': 42.6, 'hs_m': 652, 'lon': 21.2},
    'Zagreb': {'phi': 45.8, 'hs_m': 130, 'lon': 16.0},
    'Vienna': {'phi': 48.2, 'hs_m': 193, 'lon': 16.4},
    'Paris': {'phi': 48.8, 'hs_m': 34, 'lon': 2.3},
    'Brussels': {'phi': 50.8, 'hs_m': 76, 'lon': 4.3},
    'London': {'phi': 51.5, 'hs_m': 14, 'lon': -0.1},
    'Berlin': {'phi': 52.5, 'hs_m': 34, 'lon': 13.4}
}

location_list = list(locations.keys()) # Adding locations dictionary to a list called location_list to easily iterate over the locations


def interpolate_coeff(f, coeff_dict): # Interpolate the a and b coefficients for the frequency f (GHz)
    """Linearly interpolate a and b coefficients for frequency f (GHz)"""
    frequencies = sorted(coeff_dict.keys()) # Sorting the frequencies to make sure the frequencies are in ascending order

    if f < frequencies[0] or f > frequencies[-1]: # Checking if the frequency is out of range
        raise ValueError(f"Frequency {f} GHz is out of range [{frequencies[0]}-{frequencies[-1]}]") # Raising an error if the frequency is out of range

    if f in coeff_dict: # Checking if the frequency is in the coefficients dictionary
        return coeff_dict[f]['a'], coeff_dict[f]['b'] # Returning the a and b coefficients for the frequency f

    for i in range(len(frequencies) - 1):
        if frequencies[i] <= f <= frequencies[i + 1]: # Checking if the frequency is in the range of the two frequencies
            low_f, high_f = frequencies[i], frequencies[i + 1] # Assigning the low and high frequencies
            low_a, low_b = coeff_dict[low_f]['a'], coeff_dict[low_f]['b'] # Assigning the low and high a and b coefficients
            high_a, high_b = coeff_dict[high_f]['a'], coeff_dict[high_f]['b'] # Assigning the high and low a and b coefficients

            frac = (f - low_f) / (high_f - low_f) # Calculating the fraction of the frequency between the two frequencies. This is used to interpolate the a and b coefficients.
            a = low_a + (high_a - low_a) * frac
            b = low_b + (high_b - low_b) * frac

            return a, b

    return coeff_dict[f]['a'], coeff_dict[f]['b']


def calculate_rain_attenuation(f, pol, R, phi, hs_km, epsilon0):
    """Calculate rain attenuation using ITU-R P.618 model"""
    if not (1.0 <= f <= 4.0):
        raise ValueError(f"Frequency {f} GHz out of range [1.0-4.0]")
    if pol not in ['h', 'v']:
        raise ValueError("Polarization must be 'h' or 'v'")
    if R < 0:
        raise ValueError("Rain rate must be non-negative")
    if not (MIN_ELEVATION <= epsilon0 <= 90):
        raise ValueError(f"Elevation angle must be between {MIN_ELEVATION}° and 90°")

    coeff_dict = coeff_v if pol == 'v' else coeff_h
    a, b = interpolate_coeff(f, coeff_dict)
    gamma = a * (R ** b)

    if phi > LAT_THRESHOLD:
        h_r = RAIN_HEIGHT_BASE - RAIN_HEIGHT_COEFF * (phi - LAT_THRESHOLD)
    else:
        h_r = RAIN_HEIGHT_BASE

    epsilon0_rad = math.radians(epsilon0)
    sin_epsilon = math.sin(epsilon0_rad)
    l_r = (h_r - hs_km) / sin_epsilon

    exp_term = math.exp(EXP_COEFFICIENT * R)
    denominator = REDUCTION_DENOMINATOR * exp_term
    s = 1 / (1 + (l_r * sin_epsilon) / denominator)

    A_R = gamma * s * l_r

    return {
        'gamma': gamma,
        'h_r': h_r,
        'l_r': l_r,
        's': s,
        'A_R': A_R
    }


def get_location_data(location):
    """Extract latitude and height data for a given location"""
    if location not in locations:
        raise ValueError(f"Invalid location: {location}")
    return locations[location]['phi'], locations[location]['hs_m'] / 1000


def draw_europe_map(ax):
    """Load and display Europe map image"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(script_dir, 'europe_countries.jpg')

    # Load and display the map image
    img = plt.imread(map_path)
    # Set extent to match European coordinates (lon_min, lon_max, lat_min, lat_max)
    ax.imshow(img, extent=[-11, 23, 36, 56], aspect='auto', zorder=0)


# Initialize the GUI
fig = plt.figure(figsize=(16, 9))
fig.canvas.manager.set_window_title('Rain Attenuation Calculator')

# Create axes for plot and controls
ax_plot = plt.axes([0.08, 0.42, 0.55, 0.53])
ax_map = plt.axes([0.68, 0.50, 0.28, 0.45])
ax_location = plt.axes([0.05, 0.05, 0.15, 0.25])
ax_freq = plt.axes([0.30, 0.32, 0.25, 0.03])
ax_rain = plt.axes([0.30, 0.27, 0.25, 0.03])
ax_elev = plt.axes([0.30, 0.22, 0.25, 0.03])
ax_pol = plt.axes([0.60, 0.22, 0.12, 0.15])
ax_latalt = plt.axes([0.75, 0.22, 0.20, 0.15])
ax_text = plt.axes([0.22, 0.13, 0.65, 0.06])
ax_button = plt.axes([0.30, 0.05, 0.25, 0.05])
ax_text.axis('off')
ax_latalt.axis('off')

# Create widgets
slider_freq = Slider(ax_freq, 'Frequency (GHz)', 1.0, 4.0, valinit=2.5, valstep=0.1)
slider_rain = Slider(ax_rain, 'Rain Rate (mm/h)', 0, 100, valinit=30, valstep=1)
slider_elev = Slider(ax_elev, 'Elevation (°)', 1, 90, valinit=15, valstep=1)
radio_pol = RadioButtons(ax_pol, ['h', 'v'], active=1)
radio_location = RadioButtons(ax_location, location_list, active=0)
button_calc = Button(ax_button, 'Calculate')


def update_plot(event=None):
    """Calculate and update the plot"""
    try:
        # Get current values
        location = radio_location.value_selected
        f = slider_freq.val
        pol = radio_pol.value_selected
        R = slider_rain.val
        epsilon0 = slider_elev.val

        phi, hs_km = get_location_data(location)
        results = calculate_rain_attenuation(f, pol, R, phi, hs_km, epsilon0)

        # Update lat/alt display
        ax_latalt.clear()
        ax_latalt.axis('off')
        hs_m = locations[location]['hs_m']
        latalt_text = (
            f"Selected Location:\n"
            f"Latitude: {phi}° \n"
            f"Altitude: {hs_m} m"
        )
        ax_latalt.text(0.5, 0.5, latalt_text, ha='center', va='center',
                      fontsize=10, weight='bold',
                      bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))

        # Update text results
        ax_text.clear()
        ax_text.axis('off')
        result_text = (
            f"Results for {location} (f={f} GHz, pol={pol}, R={R} mm/h, ε0={epsilon0}°):\n"
            f"Specific Attenuation: {results['gamma']:.5f} dB/km  |  "
            f"Reduction Factor: {results['s']:.4f}  |  "
            f"Attenuation: {results['A_R']:.4f} dB"
        )
        ax_text.text(0.5, 0.5, result_text, ha='center', va='center',
                    fontsize=10, weight='bold',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        # Calculate for all locations
        cities = []
        a_r_values = []
        for city in location_list:
            phi_city, hs_km_city = get_location_data(city)
            results_city = calculate_rain_attenuation(f, pol, R, phi_city, hs_km_city, epsilon0)
            cities.append(city)
            a_r_values.append(results_city['A_R'])

        # Update plot
        ax_plot.clear()
        colors = ['orange' if city == location else 'skyblue' for city in cities]

        bars = ax_plot.bar(cities, a_r_values, color=colors)

        # Set alpha individually for each bar
        for i, bar in enumerate(bars):
            if cities[i] == location:
                bar.set_alpha(1.0)
            else:
                bar.set_alpha(0.7)

        ax_plot.set_xlabel('Location', fontsize=11)
        ax_plot.set_ylabel('Rain Attenuation A_R (dB)', fontsize=11)
        ax_plot.set_title(f'Rain Attenuation Across Locations\n(f={f} GHz, pol={pol}, R={R} mm/h, ε0={epsilon0}°)',
                         fontsize=12, weight='bold')
        ax_plot.tick_params(axis='x', rotation=45)
        ax_plot.grid(axis='y', alpha=0.3)

        # Add legend
        orange_patch = mpatches.Patch(color='orange', label='Selected Location')
        blue_patch = mpatches.Patch(color='skyblue', alpha=0.7, label='Other Locations')
        ax_plot.legend(handles=[orange_patch, blue_patch], loc='upper right')

        # Update map with city locations
        ax_map.clear()

        # Draw Europe map outline first
        draw_europe_map(ax_map)

        # Plot all cities
        for city in location_list:
            city_lon = locations[city]['lon']
            city_lat = locations[city]['phi']

            if city == location:
                # Selected city - larger orange marker
                ax_map.scatter(city_lon, city_lat, s=200, c='orange', marker='o',
                             edgecolors='darkred', linewidths=2, zorder=5)
                ax_map.text(city_lon, city_lat - 1, city, ha='center', va='top',
                          fontsize=8, weight='bold', color='darkred')
            else:
                # Other cities - smaller blue markers
                ax_map.scatter(city_lon, city_lat, s=80, c='skyblue', marker='o',
                             edgecolors='blue', linewidths=1, alpha=0.7, zorder=3)
                ax_map.text(city_lon, city_lat - 1, city, ha='center', va='top',
                          fontsize=7, color='navy', alpha=0.7)

        # Map styling
        ax_map.set_xlim(-11, 23)
        ax_map.set_ylim(36, 56)
        ax_map.set_xlabel('Longitude (°E)', fontsize=9)
        ax_map.set_ylabel('Latitude (°N)', fontsize=9)
        ax_map.set_title('European Locations Map', fontsize=10, weight='bold')
        ax_map.grid(True, alpha=0.3, linestyle='--', color='white', linewidth=0.5)

        fig.canvas.draw_idle()

    except Exception as e:
        ax_text.clear()
        ax_text.axis('off')
        ax_text.text(0.5, 0.5, f'Error: {str(e)}', ha='center', va='center',
                    color='red', fontsize=10, weight='bold')
        fig.canvas.draw_idle()


# Connect button to update function
button_calc.on_clicked(update_plot)

# Initial plot
update_plot()

# Show the GUI
plt.show()
