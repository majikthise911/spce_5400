#!/usr/bin/env python3
"""
Rain Attenuation Calculator - Streamlit Dashboard

A beautiful web interface for calculating rain attenuation using the ITU-R P.618 model.

Usage:
    streamlit run rain_attenuation_dashboard_fixed.py

Requirements:
    pip install streamlit plotly pandas
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from rain_attenuation import RainAttenuationCalculator

# Extended location data with longitude for mapping
LOCATION_COORDS = {
    'Madrid': {'phi': 40.4, 'hs_m': 588, 'lon': -3.7},
    'Tirana': {'phi': 41.3, 'hs_m': 104, 'lon': 19.8},
    'Rome': {'phi': 41.9, 'hs_m': 14, 'lon': 12.5},
    'Pristina': {'phi': 42.6, 'hs_m': 652, 'lon': 21.2},
    'Zagreb': {'phi': 45.8, 'hs_m': 130, 'lon': 16.0},
    'Vienna': {'phi': 48.2, 'hs_m': 193, 'lon': 16.4},
    'Paris': {'phi': 48.8, 'hs_m': 34, 'lon': 2.3},
    'Brussels': {'phi': 50.8, 'hs_m': 76, 'lon': 4.4},
    'London': {'phi': 51.5, 'hs_m': 14, 'lon': -0.1},
    'Berlin': {'phi': 52.5, 'hs_m': 34, 'lon': 13.4}
}

# Page configuration
st.set_page_config(
    page_title="Rain Attenuation Calculator",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize calculator (compatible with all Streamlit versions)
if 'calculator' not in st.session_state:
    st.session_state.calculator = RainAttenuationCalculator()

calc = st.session_state.calculator

# Function to create interactive map
def create_location_map(selected_city=None, all_results=None, show_all=False):
    """Create an interactive map showing cities and optionally attenuation results."""

    if show_all and all_results:
        # Map with all cities colored by attenuation
        map_data = []
        for city, data in all_results.items():
            coords = LOCATION_COORDS[city]
            map_data.append({
                'City': city,
                'Latitude': coords['phi'],
                'Longitude': coords['lon'],
                'Attenuation (dB)': data['A_R'],
                'Height (m)': coords['hs_m'],
                'Specific Attenuation': f"{data['gamma']:.6f} dB/km",
                'Reduction Factor': f"{data['s']:.4f}"
            })

        df_map = pd.DataFrame(map_data)

        # Create scatter map with color scale
        fig = px.scatter_geo(
            df_map,
            lat='Latitude',
            lon='Longitude',
            color='Attenuation (dB)',
            size='Attenuation (dB)',
            hover_name='City',
            hover_data={
                'Height (m)': True,
                'Specific Attenuation': True,
                'Reduction Factor': True,
                'Latitude': ':.1f',
                'Longitude': ':.1f'
            },
            color_continuous_scale='Reds',
            size_max=20,
            title='Rain Attenuation Across European Cities'
        )

    elif selected_city:
        # Map with single selected city
        coords = LOCATION_COORDS[selected_city]

        fig = go.Figure()
        fig.add_trace(go.Scattergeo(
            lon=[coords['lon']],
            lat=[coords['phi']],
            text=[selected_city],
            mode='markers+text',
            marker=dict(
                size=15,
                color='red',
                symbol='circle'
            ),
            textposition="top center",
            name=selected_city
        ))

        fig.update_layout(
            title=f'Selected Location: {selected_city}',
            geo=dict(
                projection_type='orthographic',
                showland=True,
                landcolor='lightgray',
                showocean=True,
                oceancolor='lightblue'
            )
        )

    else:
        # Map with all available cities
        cities = list(LOCATION_COORDS.keys())
        lats = [LOCATION_COORDS[city]['phi'] for city in cities]
        lons = [LOCATION_COORDS[city]['lon'] for city in cities]
        heights = [LOCATION_COORDS[city]['hs_m'] for city in cities]

        fig = px.scatter_geo(
            lat=lats,
            lon=lons,
            text=cities,
            hover_name=cities,
            hover_data={'Height (m)': heights},
            title='Available European Cities'
        )

        fig.update_traces(
            marker=dict(size=10, color='blue'),
            textposition="top center"
        )

    # Common layout updates
    fig.update_geos(
        projection_type="natural earth",
        showland=True,
        landcolor="lightgray",
        showocean=True,
        oceancolor="lightblue",
        showlakes=True,
        lakecolor="lightblue",
        showcountries=True,
        countrycolor="white"
    )

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=50, b=0)
    )

    return fig

# Main title
st.markdown('<h1 class="main-header">🌧️ Rain Attenuation Calculator</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #7f8c8d;">ITU-R P.618 Model for Satellite Communication Links</p>', unsafe_allow_html=True)

# Sidebar for parameters
st.sidebar.markdown("## 📡 Link Parameters")

# Parameter inputs
frequency = st.sidebar.slider(
    "🔗 Frequency (GHz)",
    min_value=1.0,
    max_value=4.0,
    value=2.5,
    step=0.1,
    help="Operating frequency of the satellite link"
)

polarization = st.sidebar.selectbox(
    "📶 Polarization",
    options=['v', 'h'],
    format_func=lambda x: 'Vertical' if x == 'v' else 'Horizontal',
    help="Antenna polarization: Vertical or Horizontal"
)

rain_rate = st.sidebar.slider(
    "🌧️ Rain Rate (mm/h)",
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    step=1.0,
    help="Rainfall intensity exceeded for the required percentage of time"
)

elevation_angle = st.sidebar.slider(
    "📐 Elevation Angle (°)",
    min_value=1.0,
    max_value=90.0,
    value=15.0,
    step=1.0,
    help="Elevation angle of the satellite from the ground station"
)

# Location selection
st.sidebar.markdown("## 🌍 Location")
location_mode = st.sidebar.radio(
    "Select location mode:",
    options=["Predefined City", "Custom Coordinates", "All Cities Comparison"]
)

if location_mode == "Predefined City":
    selected_location = st.sidebar.selectbox(
        "🏙️ Select City",
        options=list(calc.locations.keys()),
        index=0
    )
elif location_mode == "Custom Coordinates":
    custom_lat = st.sidebar.number_input(
        "📍 Latitude (°)",
        min_value=-90.0,
        max_value=90.0,
        value=45.0,
        help="Latitude in degrees (positive for North)"
    )
    custom_lon = st.sidebar.number_input(
        "📍 Longitude (°)",
        min_value=-180.0,
        max_value=180.0,
        value=10.0,
        help="Longitude in degrees (positive for East)"
    )
    custom_height = st.sidebar.number_input(
        "⛰️ Height (km)",
        min_value=0.0,
        max_value=10.0,
        value=0.5,
        help="Height above sea level in kilometers"
    )

# Show preview map
st.markdown('<h2 class="sub-header">🗺️ Location Preview</h2>', unsafe_allow_html=True)

if location_mode == "Predefined City":
    preview_map = create_location_map(selected_city=selected_location)
    st.plotly_chart(preview_map)
elif location_mode == "Custom Coordinates":
    # Create map with custom location
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon=[custom_lon],
        lat=[custom_lat],
        text=[f"Custom ({custom_lat}°N, {custom_lon}°E, {custom_height}km)"],
        mode='markers+text',
        marker=dict(size=15, color='green', symbol='circle'),
        textposition="top center"
    ))
    fig.update_geos(
        projection_type="natural earth",
        showland=True, landcolor="lightgray",
        showocean=True, oceancolor="lightblue",
        showcountries=True, countrycolor="white"
    )
    fig.update_layout(
        title='Custom Location',
        height=400,
        margin=dict(l=0, r=0, t=50, b=0)
    )
    st.plotly_chart(fig)
else:
    preview_map = create_location_map()
    st.plotly_chart(preview_map)

# Main content area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    calculate_button = st.button("🚀 Calculate Rain Attenuation")

# Results display (outside column context to avoid nesting)
if calculate_button:
    if location_mode == "Predefined City":
        # Single location calculation
        try:
            results = calc.calculate_for_location(
                frequency, polarization, rain_rate, selected_location, elevation_angle
            )

            # Display results
            st.markdown('<h2 class="sub-header">📊 Results</h2>', unsafe_allow_html=True)

            # Key metrics
            metric_cols = st.columns(4)

            with metric_cols[0]:
                st.metric(
                    label="🎯 Total Attenuation",
                    value=f"{results['A_R']:.4f} dB",
                    help="Total rain attenuation on the link"
                )

            with metric_cols[1]:
                st.metric(
                    label="⚡ Specific Attenuation",
                    value=f"{results['gamma']:.6f} dB/km",
                    help="Attenuation per kilometer of path"
                )

            with metric_cols[2]:
                st.metric(
                    label="📉 Reduction Factor",
                    value=f"{results['s']:.4f}",
                    help="Horizontal path reduction factor"
                )

            with metric_cols[3]:
                st.metric(
                    label="📏 Path Length",
                    value=f"{results['l_r']:.2f} km",
                    help="Slant path length through rain"
                )

            # Additional details
            st.markdown('<h3 class="sub-header">🔍 Calculation Details</h3>', unsafe_allow_html=True)

            details_col1, details_col2 = st.columns(2)

            with details_col1:
                st.markdown(f"""
                <div class="info-box">
                <h4>📍 Location Information</h4>
                <ul>
                    <li><strong>City:</strong> {selected_location}</li>
                    <li><strong>Latitude:</strong> {results['latitude']:.1f}°</li>
                    <li><strong>Height:</strong> {results['height_km']:.3f} km</li>
                    <li><strong>Rain Height:</strong> {results['h_r']:.3f} km</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)

            with details_col2:
                st.markdown(f"""
                <div class="info-box">
                <h4>📡 Link Parameters</h4>
                <ul>
                    <li><strong>Frequency:</strong> {frequency} GHz</li>
                    <li><strong>Polarization:</strong> {'Vertical' if polarization == 'v' else 'Horizontal'}</li>
                    <li><strong>Rain Rate:</strong> {rain_rate} mm/h</li>
                    <li><strong>Elevation:</strong> {elevation_angle}°</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error in calculation: {str(e)}")

    elif location_mode == "Custom Coordinates":
        # Custom coordinates calculation
        try:
            results = calc.calculate_rain_attenuation(
                frequency, polarization, rain_rate, custom_lat, custom_height, elevation_angle
            )

            st.markdown('<h2 class="sub-header">📊 Results for Custom Location</h2>', unsafe_allow_html=True)

            # Key metrics
            metric_cols = st.columns(4)

            with metric_cols[0]:
                st.metric(
                    label="🎯 Total Attenuation",
                    value=f"{results['A_R']:.4f} dB"
                )

            with metric_cols[1]:
                st.metric(
                    label="⚡ Specific Attenuation",
                    value=f"{results['gamma']:.6f} dB/km"
                )

            with metric_cols[2]:
                st.metric(
                    label="📉 Reduction Factor",
                    value=f"{results['s']:.4f}"
                )

            with metric_cols[3]:
                st.metric(
                    label="📏 Path Length",
                    value=f"{results['l_r']:.2f} km"
                )

            st.info(f"📍 **Custom Location:** {custom_lat}°N, {custom_lon}°E, {custom_height} km altitude")

        except Exception as e:
            st.error(f"❌ Error in calculation: {str(e)}")

    else:  # All Cities Comparison
        # Calculate for all locations
        try:
            all_results = calc.calculate_all_locations(
                frequency, polarization, rain_rate, elevation_angle
            )

            st.markdown('<h2 class="sub-header">🌍 All Cities Comparison</h2>', unsafe_allow_html=True)

            # Show results map first
            results_map = create_location_map(all_results=all_results, show_all=True)
            st.plotly_chart(results_map)

            # Create DataFrame for plotting
            df_data = []
            for city, data in all_results.items():
                df_data.append({
                    'City': city,
                    'Attenuation (dB)': data['A_R'],
                    'Latitude': data['latitude'],
                    'Height (km)': data['height_km'],
                    'Specific Attenuation (dB/km)': data['gamma'],
                    'Reduction Factor': data['s']
                })

            df = pd.DataFrame(df_data)

            # Interactive bar chart
            fig_bar = px.bar(
                df,
                x='City',
                y='Attenuation (dB)',
                title=f'Rain Attenuation Comparison (f={frequency}GHz, pol={polarization}, R={rain_rate}mm/h, elev={elevation_angle}°)',
                color='Attenuation (dB)',
                color_continuous_scale='Blues',
                hover_data=['Latitude', 'Height (km)']
            )
            fig_bar.update_layout(
                xaxis_tickangle=-45,
                height=500,
                showlegend=False
            )
            st.plotly_chart(fig_bar)

            # Scatter plot: Latitude vs Attenuation
            fig_scatter = px.scatter(
                df,
                x='Latitude',
                y='Attenuation (dB)',
                size='Height (km)',
                hover_name='City',
                title='Attenuation vs Latitude (bubble size = height)',
                color='Attenuation (dB)',
                color_continuous_scale='Viridis'
            )
            fig_scatter.update_layout(height=400)
            st.plotly_chart(fig_scatter)

            # Data table
            st.markdown('<h3 class="sub-header">📋 Detailed Results Table</h3>', unsafe_allow_html=True)
            st.dataframe(
                df.round(6),
                height=300
            )

            # Summary statistics
            st.markdown('<h3 class="sub-header">📈 Summary Statistics</h3>', unsafe_allow_html=True)
            summary_cols = st.columns(4)

            with summary_cols[0]:
                st.metric("🔝 Max Attenuation", f"{df['Attenuation (dB)'].max():.4f} dB")

            with summary_cols[1]:
                st.metric("🔻 Min Attenuation", f"{df['Attenuation (dB)'].min():.4f} dB")

            with summary_cols[2]:
                st.metric("📊 Average", f"{df['Attenuation (dB)'].mean():.4f} dB")

            with summary_cols[3]:
                st.metric("📏 Std Dev", f"{df['Attenuation (dB)'].std():.4f} dB")

        except Exception as e:
            st.error(f"❌ Error in calculation: {str(e)}")

# Footer with information
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d;">
<h4>ℹ️ About This Calculator</h4>
<p>This tool implements the ITU-R P.618 recommendation for calculating rain attenuation in satellite communication links.</p>

<p><strong>🔗 Key Features:</strong> ITU-R P.618 compliant calculations • Support for frequencies 1-4 GHz •
Predefined European city locations • Custom coordinate support • Interactive visualizations</p>

<p style="margin-top: 1rem;"><em>Built with Streamlit and Plotly • Data source: ITU-R P.618 Tables 2.1 & 2.5</em></p>
</div>
""", unsafe_allow_html=True)

# Sidebar information
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Quick Help")
st.sidebar.markdown("""
**Frequency Range:** 1-4 GHz
**Polarization:** V = Vertical, H = Horizontal
**Rain Rate:** Rainfall intensity exceeded for required % of time
**Elevation Angle:** Angle from horizontal to satellite
""")

st.sidebar.markdown("### 🏙️ Available Cities")
cities_text = "  \n".join([f"• {city}" for city in calc.locations.keys()])
st.sidebar.markdown(cities_text)