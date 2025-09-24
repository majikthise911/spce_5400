#!/usr/bin/env python3
"""
Rain Attenuation Core Calculator

Implementation of the ITU-R P.618 model for calculating rain attenuation
on satellite communication links.
"""

import numpy as np
import math

class RainAttenuationCalculator:
    """
    Rain attenuation calculator implementing ITU-R P.618 model.
    """
    
    def __init__(self):
        """Initialize the calculator with predefined locations."""
        self.locations = {
            # Europe
            'Madrid': {'phi': 40.4, 'hs_m': 588, 'lon': -3.7},
            'Tirana': {'phi': 41.3, 'hs_m': 104, 'lon': 19.8},
            'Rome': {'phi': 41.9, 'hs_m': 14, 'lon': 12.5},
            'Pristina': {'phi': 42.6, 'hs_m': 652, 'lon': 21.2},
            'Zagreb': {'phi': 45.8, 'hs_m': 130, 'lon': 16.0},
            'Vienna': {'phi': 48.2, 'hs_m': 193, 'lon': 16.4},
            'Paris': {'phi': 48.8, 'hs_m': 34, 'lon': 2.3},
            'Brussels': {'phi': 50.8, 'hs_m': 76, 'lon': 4.4},
            'London': {'phi': 51.5, 'hs_m': 14, 'lon': -0.1},
            'Berlin': {'phi': 52.5, 'hs_m': 34, 'lon': 13.4},
            'Amsterdam': {'phi': 52.4, 'hs_m': -2, 'lon': 4.9},
            'Stockholm': {'phi': 59.3, 'hs_m': 28, 'lon': 18.1},
            'Helsinki': {'phi': 60.2, 'hs_m': 26, 'lon': 24.9},
            'Moscow': {'phi': 55.8, 'hs_m': 156, 'lon': 37.6},
            'Athens': {'phi': 37.9, 'hs_m': 170, 'lon': 23.7},
            'Lisbon': {'phi': 38.7, 'hs_m': 56, 'lon': -9.1},
            'Copenhagen': {'phi': 55.7, 'hs_m': 24, 'lon': 12.6},
            'Oslo': {'phi': 59.9, 'hs_m': 23, 'lon': 10.8},
            'Warsaw': {'phi': 52.2, 'hs_m': 107, 'lon': 21.0},
            'Prague': {'phi': 50.1, 'hs_m': 235, 'lon': 14.4},
            
            # North America
            'New York': {'phi': 40.7, 'hs_m': 10, 'lon': -74.0},
            'Los Angeles': {'phi': 34.1, 'hs_m': 71, 'lon': -118.2},
            'Chicago': {'phi': 41.9, 'hs_m': 179, 'lon': -87.6},
            'Houston': {'phi': 29.8, 'hs_m': 12, 'lon': -95.4},
            'Phoenix': {'phi': 33.4, 'hs_m': 331, 'lon': -112.1},
            'Philadelphia': {'phi': 39.9, 'hs_m': 12, 'lon': -75.2},
            'San Antonio': {'phi': 29.4, 'hs_m': 198, 'lon': -98.5},
            'San Diego': {'phi': 32.7, 'hs_m': 19, 'lon': -117.2},
            'Dallas': {'phi': 32.8, 'hs_m': 131, 'lon': -96.8},
            'San Jose': {'phi': 37.3, 'hs_m': 25, 'lon': -121.9},
            'Austin': {'phi': 30.3, 'hs_m': 149, 'lon': -97.7},
            'Seattle': {'phi': 47.6, 'hs_m': 56, 'lon': -122.3},
            'Denver': {'phi': 39.7, 'hs_m': 1655, 'lon': -105.0},
            'Boston': {'phi': 42.4, 'hs_m': 43, 'lon': -71.1},
            'Las Vegas': {'phi': 36.2, 'hs_m': 610, 'lon': -115.1},
            'Toronto': {'phi': 43.7, 'hs_m': 76, 'lon': -79.4},
            'Vancouver': {'phi': 49.3, 'hs_m': 70, 'lon': -123.1},
            'Montreal': {'phi': 45.5, 'hs_m': 36, 'lon': -73.6},
            'Mexico City': {'phi': 19.4, 'hs_m': 2240, 'lon': -99.1},
            'Guadalajara': {'phi': 20.7, 'hs_m': 1566, 'lon': -103.4},
            
            # Asia
            'Tokyo': {'phi': 35.7, 'hs_m': 44, 'lon': 139.7},
            'Shanghai': {'phi': 31.2, 'hs_m': 4, 'lon': 121.5},
            'Beijing': {'phi': 39.9, 'hs_m': 59, 'lon': 116.4},
            'Seoul': {'phi': 37.6, 'hs_m': 38, 'lon': 127.0},
            'Mumbai': {'phi': 19.1, 'hs_m': 8, 'lon': 72.9},
            'Delhi': {'phi': 28.7, 'hs_m': 216, 'lon': 77.1},
            'Bangkok': {'phi': 13.8, 'hs_m': 2, 'lon': 100.5},
            'Singapore': {'phi': 1.4, 'hs_m': 15, 'lon': 103.8},
            'Jakarta': {'phi': -6.2, 'hs_m': 7, 'lon': 106.8},
            'Manila': {'phi': 14.6, 'hs_m': 13, 'lon': 120.9},
            'Kuala Lumpur': {'phi': 3.2, 'hs_m': 66, 'lon': 101.7},
            'Hong Kong': {'phi': 22.3, 'hs_m': 552, 'lon': 114.2},
            'Taipei': {'phi': 25.0, 'hs_m': 9, 'lon': 121.6},
            'Ho Chi Minh City': {'phi': 10.8, 'hs_m': 5, 'lon': 106.7},
            'Dhaka': {'phi': 23.8, 'hs_m': 8, 'lon': 90.4},
            'Karachi': {'phi': 24.9, 'hs_m': 10, 'lon': 67.0},
            'Islamabad': {'phi': 33.7, 'hs_m': 507, 'lon': 73.1},
            'Colombo': {'phi': 6.9, 'hs_m': 1, 'lon': 79.8},
            'Almaty': {'phi': 43.2, 'hs_m': 848, 'lon': 76.9},
            'Tashkent': {'phi': 41.3, 'hs_m': 455, 'lon': 69.2},
            
            # Middle East
            'Dubai': {'phi': 25.3, 'hs_m': 5, 'lon': 55.3},
            'Riyadh': {'phi': 24.7, 'hs_m': 612, 'lon': 46.7},
            'Tehran': {'phi': 35.7, 'hs_m': 1190, 'lon': 51.4},
            'Istanbul': {'phi': 41.0, 'hs_m': 39, 'lon': 28.9},
            'Tel Aviv': {'phi': 32.1, 'hs_m': 37, 'lon': 34.8},
            'Doha': {'phi': 25.3, 'hs_m': 10, 'lon': 51.5},
            'Kuwait City': {'phi': 29.4, 'hs_m': 55, 'lon': 47.9},
            'Baghdad': {'phi': 33.3, 'hs_m': 34, 'lon': 44.4},
            'Amman': {'phi': 31.9, 'hs_m': 757, 'lon': 35.9},
            'Beirut': {'phi': 33.9, 'hs_m': 56, 'lon': 35.5},
            
            # Africa
            'Cairo': {'phi': 30.0, 'hs_m': 74, 'lon': 31.2},
            'Lagos': {'phi': 6.5, 'hs_m': 39, 'lon': 3.4},
            'Johannesburg': {'phi': -26.2, 'hs_m': 1753, 'lon': 28.0},
            'Cape Town': {'phi': -33.9, 'hs_m': 42, 'lon': 18.4},
            'Nairobi': {'phi': -1.3, 'hs_m': 1795, 'lon': 36.8},
            'Casablanca': {'phi': 33.6, 'hs_m': 50, 'lon': -7.6},
            'Algiers': {'phi': 36.7, 'hs_m': 224, 'lon': 3.2},
            'Tunis': {'phi': 36.8, 'hs_m': 4, 'lon': 10.2},
            'Addis Ababa': {'phi': 9.1, 'hs_m': 2355, 'lon': 38.7},
            'Kinshasa': {'phi': -4.4, 'hs_m': 240, 'lon': 15.3},
            'Dakar': {'phi': 14.7, 'hs_m': 22, 'lon': -17.4},
            'Accra': {'phi': 5.6, 'hs_m': 61, 'lon': -0.2},
            'Kampala': {'phi': 0.3, 'hs_m': 1190, 'lon': 32.6},
            'Dar es Salaam': {'phi': -6.8, 'hs_m': 55, 'lon': 39.3},
            'Khartoum': {'phi': 15.5, 'hs_m': 380, 'lon': 32.5},
            
            # South America
            'São Paulo': {'phi': -23.6, 'hs_m': 760, 'lon': -46.6},
            'Rio de Janeiro': {'phi': -22.9, 'hs_m': 2, 'lon': -43.2},
            'Buenos Aires': {'phi': -34.6, 'hs_m': 6, 'lon': -58.4},
            'Lima': {'phi': -12.0, 'hs_m': 154, 'lon': -77.0},
            'Bogotá': {'phi': 4.7, 'hs_m': 2640, 'lon': -74.1},
            'Santiago': {'phi': -33.4, 'hs_m': 570, 'lon': -70.6},
            'Caracas': {'phi': 10.5, 'hs_m': 909, 'lon': -66.9},
            'Quito': {'phi': -0.2, 'hs_m': 2850, 'lon': -78.5},
            'La Paz': {'phi': -16.5, 'hs_m': 3640, 'lon': -68.1},
            'Montevideo': {'phi': -34.9, 'hs_m': 43, 'lon': -56.2},
            'Asunción': {'phi': -25.3, 'hs_m': 43, 'lon': -57.6},
            'Georgetown': {'phi': 6.8, 'hs_m': 3, 'lon': -58.2},
            'Paramaribo': {'phi': 5.9, 'hs_m': 3, 'lon': -55.2},
            'Brasília': {'phi': -15.8, 'hs_m': 1172, 'lon': -47.9},
            'Medellín': {'phi': 6.2, 'hs_m': 1495, 'lon': -75.6},
            
            # Oceania
            'Sydney': {'phi': -33.9, 'hs_m': 19, 'lon': 151.2},
            'Melbourne': {'phi': -37.8, 'hs_m': 31, 'lon': 144.9},
            'Brisbane': {'phi': -27.5, 'hs_m': 27, 'lon': 153.0},
            'Perth': {'phi': -31.9, 'hs_m': 46, 'lon': 115.9},
            'Adelaide': {'phi': -34.9, 'hs_m': 50, 'lon': 138.6},
            'Auckland': {'phi': -36.8, 'hs_m': 196, 'lon': 174.7},
            'Wellington': {'phi': -41.3, 'hs_m': 31, 'lon': 174.8},
            'Christchurch': {'phi': -43.5, 'hs_m': 37, 'lon': 172.6},
            'Canberra': {'phi': -35.3, 'hs_m': 605, 'lon': 149.1},
            'Darwin': {'phi': -12.5, 'hs_m': 31, 'lon': 130.8},
            'Port Moresby': {'phi': -9.4, 'hs_m': 38, 'lon': 147.2},
            'Suva': {'phi': -18.1, 'hs_m': 6, 'lon': 178.4},
            'Noumea': {'phi': -22.3, 'hs_m': 69, 'lon': 166.4},
            'Papeete': {'phi': -17.5, 'hs_m': 2, 'lon': -149.6}
        }
    
    def _calculate_specific_attenuation(self, frequency, polarization, rain_rate):
        """
        Calculate specific attenuation gamma (dB/km) using ITU-R P.838.
        
        Args:
            frequency (float): Frequency in GHz
            polarization (str): 'v' for vertical, 'h' for horizontal
            rain_rate (float): Rain rate in mm/h
            
        Returns:
            float: Specific attenuation in dB/km
        """
        # ITU-R P.838 coefficients for frequency range 1-4 GHz
        if polarization == 'v':
            # Vertical polarization coefficients
            if frequency <= 2.9:
                k = 0.0001 * frequency**1.31
                alpha = 0.88 * frequency**0.22
            else:
                k = 0.00018 * frequency**0.99
                alpha = 0.93 * frequency**0.15
        else:
            # Horizontal polarization coefficients
            if frequency <= 2.9:
                k = 0.0000387 * frequency**1.33
                alpha = 0.912 * frequency**0.18
            else:
                k = 0.000154 * frequency**0.94
                alpha = 0.939 * frequency**0.09
        
        # Calculate specific attenuation
        gamma = k * (rain_rate ** alpha)
        return gamma
    
    def _calculate_rain_height(self, latitude):
        """
        Calculate rain height hr (km) using ITU-R P.839.
        
        Args:
            latitude (float): Latitude in degrees
            
        Returns:
            float: Rain height in km
        """
        phi = abs(latitude)
        
        if phi <= 36:
            hr = 5.0
        else:
            hr = 5.0 - 0.075 * (phi - 36)
        
        return max(hr, 1.0)  # Minimum 1 km
    
    def _calculate_slant_path_length(self, hr, hs, elevation_angle):
        """
        Calculate slant path length through rain lr (km).
        
        Args:
            hr (float): Rain height in km
            hs (float): Station height in km
            elevation_angle (float): Elevation angle in degrees
            
        Returns:
            float: Slant path length in km
        """
        theta = math.radians(elevation_angle)
        
        if hr <= hs:
            return 0.0
        
        # Slant path length
        lr = (hr - hs) / math.sin(theta)
        return lr
    
    def _calculate_horizontal_reduction_factor(self, lr, latitude, frequency, rain_rate):
        """
        Calculate horizontal path reduction factor s.
        
        Args:
            lr (float): Slant path length in km
            latitude (float): Latitude in degrees
            frequency (float): Frequency in GHz
            rain_rate (float): Rain rate in mm/h
            
        Returns:
            float: Reduction factor s
        """
        phi = abs(latitude)
        
        # Calculate effective path length
        if phi < 36:
            chi = 36 - phi
        else:
            chi = 0
        
        # Horizontal projection
        lg = lr * math.cos(math.radians(max(1, 90 - phi)))
        
        # Reduction factor calculation
        if rain_rate >= 100:
            s1 = 1.0 / (1.0 + 0.000001 * frequency * lg)
        else:
            s1 = 1.0 / (1.0 + 0.0001 * frequency * lg * (rain_rate ** 0.5))
        
        return max(s1, 0.1)  # Minimum reduction factor
    
    def calculate_rain_attenuation(self, frequency, polarization, rain_rate, latitude, height_km, elevation_angle):
        """
        Calculate rain attenuation using ITU-R P.618 model.
        
        Args:
            frequency (float): Frequency in GHz
            polarization (str): 'v' for vertical, 'h' for horizontal
            rain_rate (float): Rain rate in mm/h
            latitude (float): Latitude in degrees
            height_km (float): Station height in km
            elevation_angle (float): Elevation angle in degrees
            
        Returns:
            dict: Dictionary containing all calculation results
        """
        # Step 1: Calculate specific attenuation
        gamma = self._calculate_specific_attenuation(frequency, polarization, rain_rate)
        
        # Step 2: Calculate rain height
        hr = self._calculate_rain_height(latitude)
        
        # Step 3: Calculate slant path length
        lr = self._calculate_slant_path_length(hr, height_km, elevation_angle)
        
        # Step 4: Calculate horizontal reduction factor
        s = self._calculate_horizontal_reduction_factor(lr, latitude, frequency, rain_rate)
        
        # Step 5: Calculate total attenuation
        A_R = gamma * lr * s
        
        return {
            'A_R': A_R,
            'gamma': gamma,
            'h_r': hr,
            'l_r': lr,
            's': s,
            'latitude': latitude,
            'height_km': height_km
        }
    
    def calculate_for_location(self, frequency, polarization, rain_rate, location_name, elevation_angle):
        """
        Calculate rain attenuation for a predefined location.
        
        Args:
            frequency (float): Frequency in GHz
            polarization (str): 'v' for vertical, 'h' for horizontal
            rain_rate (float): Rain rate in mm/h
            location_name (str): Name of predefined location
            elevation_angle (float): Elevation angle in degrees
            
        Returns:
            dict: Dictionary containing all calculation results
        """
        if location_name not in self.locations:
            raise ValueError(f"Location '{location_name}' not found in predefined locations")
        
        location = self.locations[location_name]
        latitude = location['phi']
        height_km = location['hs_m'] / 1000.0  # Convert meters to kilometers
        
        return self.calculate_rain_attenuation(
            frequency, polarization, rain_rate, latitude, height_km, elevation_angle
        )
    
    def calculate_for_all_locations(self, frequency, polarization, rain_rate, elevation_angle):
        """
        Calculate rain attenuation for all predefined locations.
        
        Args:
            frequency (float): Frequency in GHz
            polarization (str): 'v' for vertical, 'h' for horizontal
            rain_rate (float): Rain rate in mm/h
            elevation_angle (float): Elevation angle in degrees
            
        Returns:
            dict: Dictionary with location names as keys and results as values
        """
        results = {}
        
        for location_name in self.locations.keys():
            try:
                results[location_name] = self.calculate_for_location(
                    frequency, polarization, rain_rate, location_name, elevation_angle
                )
            except Exception as e:
                results[location_name] = {'error': str(e)}
        
        return results
