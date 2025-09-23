#!/usr/bin/env python3
"""
Rain Attenuation Calculator using ITU-R P.618 Model

This module implements the ITU-R P.618 recommendation for calculating rain attenuation
in satellite communications links. It provides both a programmatic interface and
command-line functionality.

Author: Generated from Jupyter notebook
Standard: ITU-R P.618
"""

import math
import argparse
from typing import Dict, Tuple, Optional, Union


# Constants for rain attenuation model (ITU-R P.618)
MIN_ELEVATION = 1.0  # Minimum elevation angle in degrees
EXP_COEFFICIENT = -0.015  # Exponential coefficient for reduction factor
REDUCTION_DENOMINATOR = 35  # Denominator constant for reduction factor
LAT_THRESHOLD = 23  # Latitude threshold for rain height calculation
RAIN_HEIGHT_BASE = 5  # Base rain height in km
RAIN_HEIGHT_COEFF = 0.073  # Coefficient for rain height adjustment


# Table 2.1 - a and b coefficients for rain attenuation model
COEFF_VERTICAL = {
    1.0: {'a': 0.0000308, 'b': 0.8592},
    1.5: {'a': 0.0000574, 'b': 0.8957},
    2.0: {'a': 0.0000998, 'b': 0.9490},
    2.5: {'a': 0.0001464, 'b': 1.0085},
    3.0: {'a': 0.0001942, 'b': 1.0688},
    3.5: {'a': 0.0002346, 'b': 1.1387},
    4.0: {'a': 0.0002461, 'b': 1.2476}
}

COEFF_HORIZONTAL = {
    1.0: {'a': 0.0000259, 'b': 0.9691},
    1.5: {'a': 0.0000443, 'b': 1.0185},
    2.0: {'a': 0.0000847, 'b': 1.0664},
    2.5: {'a': 0.0001321, 'b': 1.1209},
    3.0: {'a': 0.0001390, 'b': 1.2322},
    3.5: {'a': 0.0001155, 'b': 1.4189},
    4.0: {'a': 0.0001071, 'b': 1.6009}
}

# Table 2.5 - European city locations with latitude and altitude
LOCATIONS = {
    'Madrid': {'phi': 40.4, 'hs_m': 588},
    'Tirana': {'phi': 41.3, 'hs_m': 104},
    'Rome': {'phi': 41.9, 'hs_m': 14},
    'Pristina': {'phi': 42.6, 'hs_m': 652},
    'Zagreb': {'phi': 45.8, 'hs_m': 130},
    'Vienna': {'phi': 48.2, 'hs_m': 193},
    'Paris': {'phi': 48.8, 'hs_m': 34},
    'Brussels': {'phi': 50.8, 'hs_m': 76},
    'London': {'phi': 51.5, 'hs_m': 14},
    'Berlin': {'phi': 52.5, 'hs_m': 34}
}


class RainAttenuationCalculator:
    """Rain attenuation calculator implementing ITU-R P.618 model."""

    def __init__(self):
        """Initialize the calculator with coefficient tables."""
        self.coeff_v = COEFF_VERTICAL
        self.coeff_h = COEFF_HORIZONTAL
        self.locations = LOCATIONS

    def interpolate_coefficients(self, frequency: float,
                               coeff_dict: Dict[float, Dict[str, float]]) -> Tuple[float, float]:
        """
        Linearly interpolate a and b coefficients for a given frequency.

        Args:
            frequency: Frequency in GHz
            coeff_dict: Dictionary containing coefficient tables

        Returns:
            Tuple of (a, b) coefficients

        Raises:
            ValueError: If frequency is out of range
        """
        frequencies = sorted(coeff_dict.keys())

        if frequency < frequencies[0] or frequency > frequencies[-1]:
            raise ValueError(
                f"Frequency {frequency} GHz is out of range "
                f"[{frequencies[0]}-{frequencies[-1]}]"
            )

        if frequency in coeff_dict:
            return coeff_dict[frequency]['a'], coeff_dict[frequency]['b']

        # Find the two frequencies that bracket the input frequency
        for i in range(len(frequencies) - 1):
            if frequencies[i] <= frequency <= frequencies[i + 1]:
                low_f, high_f = frequencies[i], frequencies[i + 1]
                low_a = coeff_dict[low_f]['a']
                low_b = coeff_dict[low_f]['b']
                high_a = coeff_dict[high_f]['a']
                high_b = coeff_dict[high_f]['b']

                # Linear interpolation
                frac = (frequency - low_f) / (high_f - low_f)
                a = low_a + (high_a - low_a) * frac
                b = low_b + (high_b - low_b) * frac

                return a, b

        # Should never reach here
        raise ValueError(f"Unable to interpolate for frequency {frequency}")

    def get_location_data(self, location: str) -> Tuple[float, float]:
        """
        Extract latitude and height data for a given location.

        Args:
            location: Location name from predefined locations

        Returns:
            Tuple of (latitude in degrees, height in km)

        Raises:
            ValueError: If location is not found
        """
        if location not in self.locations:
            available = list(self.locations.keys())
            raise ValueError(f"Invalid location: {location}. Available: {available}")

        data = self.locations[location]
        return data['phi'], data['hs_m'] / 1000.0

    def calculate_rain_attenuation(self, frequency: float, polarization: str,
                                 rain_rate: float, latitude: float,
                                 height_km: float, elevation_angle: float) -> Dict[str, float]:
        """
        Calculate rain attenuation using ITU-R P.618 model.

        Args:
            frequency: Frequency in GHz (1.0 to 4.0)
            polarization: Polarization ('h' for horizontal, 'v' for vertical)
            rain_rate: Rain rate in mm/h (non-negative)
            latitude: Latitude in degrees
            height_km: Station height above sea level in km
            elevation_angle: Elevation angle in degrees (1 to 90)

        Returns:
            Dictionary containing:
                - gamma: Specific attenuation (dB/km)
                - h_r: Effective rain height (km)
                - l_r: Slant path length (km)
                - s: Horizontal reduction factor
                - A_R: Total rain attenuation (dB)

        Raises:
            ValueError: For invalid input parameters
        """
        # Input validation
        if not (1.0 <= frequency <= 4.0):
            raise ValueError(f"Frequency {frequency} GHz out of range [1.0-4.0]")

        if polarization not in ['h', 'v']:
            raise ValueError("Polarization must be 'h' (horizontal) or 'v' (vertical)")

        if rain_rate < 0:
            raise ValueError("Rain rate must be non-negative")

        if not (MIN_ELEVATION <= elevation_angle <= 90):
            raise ValueError(
                f"Elevation angle must be between {MIN_ELEVATION}° and 90°"
            )

        # Step 1: Get a and b coefficients using interpolation
        coeff_dict = self.coeff_v if polarization == 'v' else self.coeff_h
        a, b = self.interpolate_coefficients(frequency, coeff_dict)

        # Step 2: Calculate specific attenuation gamma (dB/km)
        gamma = a * (rain_rate ** b)

        # Step 3: Calculate effective rain height h_r (km)
        if latitude > LAT_THRESHOLD:
            h_r = RAIN_HEIGHT_BASE - RAIN_HEIGHT_COEFF * (latitude - LAT_THRESHOLD)
        else:
            h_r = RAIN_HEIGHT_BASE

        # Step 4: Calculate slant path length l_r (km)
        elevation_rad = math.radians(elevation_angle)
        sin_elevation = math.sin(elevation_rad)
        l_r = (h_r - height_km) / sin_elevation

        # Step 5: Calculate horizontal reduction factor s
        exp_term = math.exp(EXP_COEFFICIENT * rain_rate)
        denominator = REDUCTION_DENOMINATOR * exp_term
        s = 1 / (1 + (l_r * sin_elevation) / denominator)

        # Step 6: Calculate total rain attenuation A_R (dB)
        A_R = gamma * s * l_r

        return {
            'gamma': gamma,
            'h_r': h_r,
            'l_r': l_r,
            's': s,
            'A_R': A_R
        }

    def calculate_for_location(self, frequency: float, polarization: str,
                             rain_rate: float, location: str,
                             elevation_angle: float) -> Dict[str, float]:
        """
        Calculate rain attenuation for a predefined location.

        Args:
            frequency: Frequency in GHz
            polarization: Polarization ('h' or 'v')
            rain_rate: Rain rate in mm/h
            location: Location name from predefined locations
            elevation_angle: Elevation angle in degrees

        Returns:
            Dictionary with calculation results including location info

        Raises:
            ValueError: For invalid inputs
        """
        latitude, height_km = self.get_location_data(location)
        results = self.calculate_rain_attenuation(
            frequency, polarization, rain_rate, latitude, height_km, elevation_angle
        )

        # Add location information to results
        results['location'] = location
        results['latitude'] = latitude
        results['height_km'] = height_km

        return results

    def calculate_all_locations(self, frequency: float, polarization: str,
                              rain_rate: float, elevation_angle: float) -> Dict[str, Dict]:
        """
        Calculate rain attenuation for all predefined locations.

        Args:
            frequency: Frequency in GHz
            polarization: Polarization ('h' or 'v')
            rain_rate: Rain rate in mm/h
            elevation_angle: Elevation angle in degrees

        Returns:
            Dictionary with location names as keys and results as values
        """
        results = {}
        for location in self.locations.keys():
            results[location] = self.calculate_for_location(
                frequency, polarization, rain_rate, location, elevation_angle
            )
        return results


def create_simple_plot(results: Dict[str, Dict], title: str = None) -> None:
    """
    Create a simple text-based bar chart of attenuation results.

    This function provides basic visualization without requiring matplotlib,
    making the module more portable.

    Args:
        results: Results dictionary from calculate_all_locations
        title: Optional title for the chart
    """
    if not results:
        print("No results to plot")
        return

    if title:
        print(f"\n{title}")
        print("=" * len(title))

    # Find max attenuation for scaling
    max_atten = max(data['A_R'] for data in results.values())
    scale_factor = 50 / max_atten if max_atten > 0 else 1

    print(f"\n{'Location':<12} {'A_R (dB)':<10} {'Bar Chart'}")
    print("-" * 60)

    for location, data in results.items():
        atten = data['A_R']
        bar_length = int(atten * scale_factor)
        bar = "#" * bar_length
        print(f"{location:<12} {atten:<10.4f} {bar}")


def main():
    """Command-line interface for the rain attenuation calculator."""
    parser = argparse.ArgumentParser(
        description="Calculate rain attenuation using ITU-R P.618 model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python rain_attenuation.py -f 2.5 -p v -r 30 -l Madrid -e 15
  python rain_attenuation.py -f 3.0 -p h -r 50 --lat 45.0 --height 0.5 -e 20
  python rain_attenuation.py -f 2.0 -p v -r 30 -e 15 --all-locations
        """
    )

    # Required arguments
    parser.add_argument('-f', '--frequency', type=float, required=True,
                       help='Frequency in GHz (1.0 to 4.0)')
    parser.add_argument('-p', '--polarization', choices=['h', 'v'], required=True,
                       help='Polarization: h (horizontal) or v (vertical)')
    parser.add_argument('-r', '--rain-rate', type=float, required=True,
                       help='Rain rate in mm/h')
    parser.add_argument('-e', '--elevation', type=float, required=True,
                       help='Elevation angle in degrees (1 to 90)')

    # Location specification (mutually exclusive)
    location_group = parser.add_mutually_exclusive_group(required=True)
    location_group.add_argument('-l', '--location',
                               choices=list(LOCATIONS.keys()),
                               help='Predefined location')
    location_group.add_argument('--lat', type=float,
                               help='Latitude in degrees (use with --height)')
    location_group.add_argument('--all-locations', action='store_true',
                               help='Calculate for all predefined locations')

    # Additional arguments
    parser.add_argument('--height', type=float,
                       help='Height above sea level in km (required with --lat)')
    parser.add_argument('--plot', action='store_true',
                       help='Show simple text plot for multiple locations')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Show detailed results')

    args = parser.parse_args()

    # Validate arguments
    if args.lat is not None and args.height is None:
        parser.error("--height is required when using --lat")

    # Create calculator
    calc = RainAttenuationCalculator()

    try:
        if args.all_locations:
            # Calculate for all locations
            results = calc.calculate_all_locations(
                args.frequency, args.polarization, args.rain_rate, args.elevation
            )

            print(f"Rain Attenuation Results")
            print(f"Frequency: {args.frequency} GHz, Polarization: {args.polarization}")
            print(f"Rain Rate: {args.rain_rate} mm/h, Elevation: {args.elevation} degrees")
            print()

            for location, data in results.items():
                print(f"{location:<12}: {data['A_R']:.4f} dB")

            if args.plot:
                title = (f"Rain Attenuation (f={args.frequency}GHz, "
                        f"pol={args.polarization}, R={args.rain_rate}mm/h, "
                        f"elevation={args.elevation} degrees)")
                create_simple_plot(results, title)

        elif args.location:
            # Calculate for specific location
            results = calc.calculate_for_location(
                args.frequency, args.polarization, args.rain_rate,
                args.location, args.elevation
            )

            print(f"Rain Attenuation for {args.location}")
            print(f"Parameters: f={args.frequency} GHz, pol={args.polarization}, "
                  f"R={args.rain_rate} mm/h, elevation={args.elevation} degrees")
            print(f"Total Attenuation: {results['A_R']:.4f} dB")

            if args.verbose:
                print(f"Specific Attenuation: {results['gamma']:.6f} dB/km")
                print(f"Reduction Factor: {results['s']:.4f}")
                print(f"Rain Height: {results['h_r']:.3f} km")
                print(f"Slant Path Length: {results['l_r']:.3f} km")

        else:
            # Calculate for custom coordinates
            results = calc.calculate_rain_attenuation(
                args.frequency, args.polarization, args.rain_rate,
                args.lat, args.height, args.elevation
            )

            print(f"Rain Attenuation for Custom Location")
            print(f"Coordinates: {args.lat} degrees N, {args.height} km altitude")
            print(f"Parameters: f={args.frequency} GHz, pol={args.polarization}, "
                  f"R={args.rain_rate} mm/h, elevation={args.elevation} degrees")
            print(f"Total Attenuation: {results['A_R']:.4f} dB")

            if args.verbose:
                print(f"Specific Attenuation: {results['gamma']:.6f} dB/km")
                print(f"Reduction Factor: {results['s']:.4f}")
                print(f"Rain Height: {results['h_r']:.3f} km")
                print(f"Slant Path Length: {results['l_r']:.3f} km")

    except ValueError as e:
        print(f"Error: {e}")
        return 1

    return 0


# Example usage and testing
if __name__ == "__main__":
    # If run as script, use command line interface
    import sys
    if len(sys.argv) > 1:
        sys.exit(main())

    # Otherwise, run some example calculations
    print("Rain Attenuation Calculator - Example Usage")
    print("=" * 50)

    calc = RainAttenuationCalculator()

    # Example 1: Vienna calculation (matches Figure 2.5)
    print("\nExample 1: Vienna calculation (Figure 2.5 validation)")
    results = calc.calculate_for_location(2.0, 'v', 30, 'Vienna', 30)
    print(f"Vienna: A_R = {results['A_R']:.6f} dB")
    print(f"Specific Attenuation: {results['gamma']:.6f} dB/km")
    print(f"Reduction Factor: {results['s']:.4f}")

    # Example 2: All locations comparison
    print("\nExample 2: All locations comparison")
    print("f=2.5 GHz, pol=v, R=30 mm/h, elevation=15 degrees")
    all_results = calc.calculate_all_locations(2.5, 'v', 30, 15)

    for location, data in all_results.items():
        print(f"{location:<12}: {data['A_R']:.4f} dB")

    # Example 3: Custom location
    print("\nExample 3: Custom location (45 degrees N, 500m altitude)")
    custom_results = calc.calculate_rain_attenuation(3.0, 'h', 25, 45.0, 0.5, 20)
    print(f"Custom location: A_R = {custom_results['A_R']:.4f} dB")