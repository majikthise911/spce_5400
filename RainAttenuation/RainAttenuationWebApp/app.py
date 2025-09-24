#!/usr/bin/env python3
"""
Rain Attenuation Calculator - Streamlit Dashboard

A beautiful web interface for calculating rain attenuation using the ITU-R P.618 model.

Usage:
    streamlit run app.py
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json
import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch
from rain_attenuation_core import RainAttenuationCalculator

# Get calculator instance and location data will be set after initialization

# Page configuration
st.set_page_config(page_title="Rain Attenuation Calculator",
                   page_icon="🌧️",
                   layout="wide",
                   initial_sidebar_state="expanded")

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
    .metric-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid #e9ecef;
    }
</style>
""",
            unsafe_allow_html=True)

# Initialize calculator
if 'calculator' not in st.session_state:
    st.session_state.calculator = RainAttenuationCalculator()

calc = st.session_state.calculator

# Use calculator's centralized location data
LOCATION_COORDS = calc.locations


# Function to create interactive map
def create_location_map(selected_city=None, all_results=None, show_all=False):
    """Create an interactive map showing cities and optionally attenuation results."""

    if show_all and all_results:
        # Map with all cities colored by attenuation
        map_data = []
        for city, data in all_results.items():
            if 'error' not in data:
                coords = LOCATION_COORDS[city]
                map_data.append({
                    'City': city,
                    'Latitude': coords['phi'],
                    'Longitude': coords['lon'],
                    'Attenuation (dB)': data['A_R'],
                    'Height (m)': coords['hs_m'],
                    'Specific Attenuation (dB/km)':
                    f"{data['gamma']:.6f} dB/km",
                    'Reduction Factor': f"{data['s']:.4f}"
                })

        if map_data:
            df_map = pd.DataFrame(map_data)

            # Create scatter map with color scale
            fig = px.scatter_geo(df_map,
                                 lat='Latitude',
                                 lon='Longitude',
                                 color='Attenuation (dB)',
                                 size='Attenuation (dB)',
                                 hover_name='City',
                                 hover_data={
                                     'Height (m)': True,
                                     'Specific Attenuation (dB/km)': True,
                                     'Reduction Factor': True,
                                     'Latitude': ':.1f',
                                     'Longitude': ':.1f'
                                 },
                                 color_continuous_scale='Reds',
                                 size_max=20,
                                 title='Rain Attenuation Across Global Cities')
        else:
            # Fallback to basic map if no valid data
            fig = create_basic_cities_map()

    elif selected_city:
        # Map with single selected city
        coords = LOCATION_COORDS[selected_city]

        fig = go.Figure()
        fig.add_trace(
            go.Scattergeo(lon=[coords['lon']],
                          lat=[coords['phi']],
                          text=[selected_city],
                          mode='markers+text',
                          marker=dict(size=15, color='red', symbol='circle'),
                          textposition="top center",
                          name=selected_city))

        fig.update_layout(title=f'Selected Location: {selected_city}',
                          geo=dict(projection_type='orthographic',
                                   showland=True,
                                   landcolor='lightgray',
                                   showocean=True,
                                   oceancolor='lightblue'))

    else:
        # Map with all available cities
        fig = create_basic_cities_map()

    # Common layout updates
    fig.update_geos(projection_type="natural earth",
                    showland=True,
                    landcolor="lightgray",
                    showocean=True,
                    oceancolor="lightblue",
                    showlakes=True,
                    lakecolor="lightblue",
                    showcountries=True,
                    countrycolor="white")

    fig.update_layout(height=500, margin=dict(l=0, r=0, t=50, b=0))

    return fig


def create_basic_cities_map():
    """Create a basic map showing all available cities."""
    cities = list(LOCATION_COORDS.keys())
    lats = [LOCATION_COORDS[city]['phi'] for city in cities]
    lons = [LOCATION_COORDS[city]['lon'] for city in cities]
    heights = [LOCATION_COORDS[city]['hs_m'] for city in cities]

    fig = px.scatter_geo(lat=lats,
                         lon=lons,
                         text=cities,
                         hover_name=cities,
                         hover_data={'Height (m)': heights},
                         title='Available Global Cities')

    fig.update_traces(marker=dict(size=10, color='blue'),
                      textposition="top center")

    return fig


def create_frequency_sensitivity_chart(calc, location_name, polarization,
                                       rain_rate, elevation_angle):
    """Create a chart showing attenuation vs frequency."""
    frequencies = np.arange(1.0, 4.1, 0.1)
    attenuations = []

    for freq in frequencies:
        try:
            result = calc.calculate_for_location(freq, polarization, rain_rate,
                                                 location_name,
                                                 elevation_angle)
            attenuations.append(result['A_R'])
        except:
            attenuations.append(0)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=frequencies,
                   y=attenuations,
                   mode='lines+markers',
                   name='Rain Attenuation',
                   line=dict(color='red', width=3),
                   marker=dict(size=6)))

    fig.update_layout(title='Rain Attenuation vs Frequency',
                      xaxis_title='Frequency (GHz)',
                      yaxis_title='Attenuation (dB)',
                      height=400)

    return fig


def create_rain_rate_sensitivity_chart(calc, location_name, frequency,
                                       polarization, elevation_angle):
    """Create a chart showing attenuation vs rain rate."""
    rain_rates = np.arange(5, 101, 5)
    attenuations = []

    for rr in rain_rates:
        try:
            result = calc.calculate_for_location(frequency, polarization, rr,
                                                 location_name,
                                                 elevation_angle)
            attenuations.append(result['A_R'])
        except:
            attenuations.append(0)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=rain_rates,
                   y=attenuations,
                   mode='lines+markers',
                   name='Rain Attenuation',
                   line=dict(color='blue', width=3),
                   marker=dict(size=6)))

    fig.update_layout(title='Rain Attenuation vs Rain Rate',
                      xaxis_title='Rain Rate (mm/h)',
                      yaxis_title='Attenuation (dB)',
                      height=400)

    return fig


# Export functionality
def export_to_csv(data, filename_base):
    """Export data to CSV format."""
    if isinstance(data, dict):
        # Convert single result to DataFrame
        df = pd.DataFrame([data])
    elif isinstance(data, pd.DataFrame):
        df = data
    else:
        # Handle list of dictionaries
        df = pd.DataFrame(data)

    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue()


def export_to_json(data, parameters=None):
    """Export data to JSON format with metadata."""
    export_data = {
        "timestamp": datetime.now().isoformat(),
        "parameters": parameters or {},
        "results": data
    }
    return json.dumps(export_data, indent=2)


def export_chart_as_png(fig, filename_base):
    """Export plotly figure as PNG."""
    try:
        img_bytes = fig.to_image(format="png", width=800, height=600)
        return img_bytes
    except Exception as e:
        st.error(f"Chart export failed: {e}")
        return None


def create_pdf_report(data, parameters, charts_data=None):
    """Create a PDF report with calculation results and charts."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer,
                            pagesize=letter,
                            leftMargin=inch,
                            rightMargin=inch)

    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('CustomTitle',
                                 parent=styles['Title'],
                                 fontSize=24,
                                 spaceAfter=30,
                                 textColor=colors.HexColor('#1f77b4'))

    # Build document content
    content = []

    # Title
    content.append(Paragraph("Rain Attenuation Calculator Report",
                             title_style))
    content.append(Spacer(1, 20))

    # Timestamp
    content.append(
        Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                  styles['Normal']))
    content.append(Spacer(1, 20))

    # Parameters section
    if parameters:
        content.append(Paragraph("Calculation Parameters", styles['Heading2']))
        param_data = []
        for key, value in parameters.items():
            param_data.append([key.replace('_', ' ').title(), str(value)])

        param_table = Table(param_data, colWidths=[2 * inch, 3 * inch])
        param_table.setStyle(
            TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 14),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        content.append(param_table)
        content.append(Spacer(1, 20))

    # Results section
    content.append(Paragraph("Calculation Results", styles['Heading2']))

    if isinstance(data, dict):
        # Single location results - get location info from parameters
        location_info = parameters.get('location', 'Custom Location')
        lat = parameters.get('latitude', data.get('latitude', 0))
        height = parameters.get('height_km', data.get('height_km', 0))

        result_data = [
            ['Parameter', 'Value',
             'Unit'], ['Location', str(location_info), ''],
            ['Latitude', f"{lat:.1f}", '°'], ['Height', f"{height:.3f}", 'km'],
            ['Total Attenuation', f"{data.get('A_R', 0):.4f}", 'dB'],
            ['Specific Attenuation', f"{data.get('gamma', 0):.6f}", 'dB/km'],
            ['Reduction Factor', f"{data.get('s', 0):.4f}", ''],
            ['Path Length', f"{data.get('l_r', 0):.2f}", 'km'],
            ['Rain Height', f"{data.get('h_r', 0):.3f}", 'km']
        ]
    elif isinstance(data, list):
        # Multiple location results
        result_data = [[
            'City', 'Attenuation (dB)', 'Specific Atten. (dB/km)',
            'Reduction Factor', 'Path Length (km)'
        ]]
        for item in data:
            if isinstance(item, dict) and 'City' in item:
                result_data.append([
                    item['City'],
                    item.get('Attenuation (dB)', 'N/A'),
                    item.get('Specific Attenuation (dB/km)', 'N/A'),
                    item.get('Reduction Factor', 'N/A'),
                    item.get('Path Length (km)', 'N/A')
                ])

    result_table = Table(result_data)
    result_table.setStyle(
        TableStyle([('BACKGROUND', (0, 0), (-1, 0),
                     colors.HexColor('#1f77b4')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('FONTSIZE', (0, 1), (-1, -1), 10)]))
    content.append(result_table)
    content.append(Spacer(1, 20))

    # Add charts if provided
    if charts_data:
        content.append(Paragraph("Analysis Charts", styles['Heading2']))
        for chart_title, chart_bytes in charts_data.items():
            if chart_bytes:
                try:
                    content.append(Paragraph(chart_title, styles['Heading3']))
                    content.append(Spacer(1, 10))

                    # Create image from bytes
                    chart_buffer = io.BytesIO(chart_bytes)
                    img = Image(chart_buffer,
                                width=6 * inch,
                                height=4.5 * inch)
                    content.append(img)
                    content.append(Spacer(1, 20))
                except Exception as e:
                    content.append(
                        Paragraph(f"Chart could not be included: {e}",
                                  styles['Normal']))

    # Build PDF
    doc.build(content)
    return buffer.getvalue()


def create_export_section(data,
                          parameters,
                          export_prefix="results",
                          charts=None):
    """Create export buttons for different formats."""
    st.markdown("### 📥 Export Results")

    # Export charts as images if provided
    charts_data = {}
    if charts:
        for chart_name, fig in charts.items():
            chart_bytes = export_chart_as_png(fig,
                                              f"{export_prefix}_{chart_name}")
            if chart_bytes:
                charts_data[chart_name] = chart_bytes

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # CSV Export
        csv_data = export_to_csv(data, export_prefix)
        st.download_button(
            label="📄 Download CSV",
            data=csv_data,
            file_name=
            f"{export_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            help="Download results as CSV file")

    with col2:
        # JSON Export
        json_data = export_to_json(data, parameters)
        st.download_button(
            label="📋 Download JSON",
            data=json_data,
            file_name=
            f"{export_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            help="Download results as JSON file with metadata")

    with col3:
        # PDF Export (with charts if available)
        pdf_data = create_pdf_report(data, parameters, charts_data)
        st.download_button(
            label="📑 Download PDF",
            data=pdf_data,
            file_name=
            f"{export_prefix}_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mime="application/pdf",
            help="Download comprehensive PDF report with charts")

    with col4:
        # Individual Charts Export
        if charts_data:
            chart_names = list(charts_data.keys())
            if len(chart_names) == 1:
                chart_bytes = charts_data[chart_names[0]]
                st.download_button(
                    label="📊 Download Chart",
                    data=chart_bytes,
                    file_name=
                    f"{export_prefix}_{chart_names[0]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
                    mime="image/png",
                    help="Download chart as PNG image")
            else:
                # Multiple charts - create a zip
                import zipfile
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    for chart_name, chart_bytes in charts_data.items():
                        zip_file.writestr(f"{chart_name}.png", chart_bytes)

                st.download_button(
                    label="📊 Download Charts",
                    data=zip_buffer.getvalue(),
                    file_name=
                    f"{export_prefix}_charts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                    mime="application/zip",
                    help="Download all charts as ZIP file")


# Main title
st.markdown('<h1 class="main-header">🌧️ Rain Attenuation Calculator</h1>',
            unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; font-size: 1.2rem; color: #7f8c8d;">ITU-R P.618 Model for Satellite Communication Links</p>',
    unsafe_allow_html=True)

# Sidebar for parameters
st.sidebar.markdown("## 📡 Link Parameters")

# Parameter inputs
frequency = st.sidebar.slider("🔗 Frequency (GHz)",
                              min_value=1.0,
                              max_value=4.0,
                              value=2.5,
                              step=0.1,
                              help="Operating frequency of the satellite link")

polarization = st.sidebar.selectbox(
    "📶 Polarization",
    options=['v', 'h'],
    format_func=lambda x: 'Vertical' if x == 'v' else 'Horizontal',
    help="Antenna polarization: Vertical or Horizontal")

rain_rate = st.sidebar.slider(
    "🌧️ Rain Rate (mm/h)",
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    step=1.0,
    help="Rainfall intensity exceeded for the required percentage of time")

elevation_angle = st.sidebar.slider(
    "📐 Elevation Angle (°)",
    min_value=1.0,
    max_value=90.0,
    value=15.0,
    step=1.0,
    help="Elevation angle of the satellite from the ground station")

# Location selection
st.sidebar.markdown("## 🌍 Location")
location_mode = st.sidebar.radio(
    "Select location mode:",
    options=["Predefined City", "Custom Coordinates", "All Cities Comparison"])

if location_mode == "Predefined City":
    selected_location = st.sidebar.selectbox("🏙️ Select City",
                                             options=list(
                                                 calc.locations.keys()),
                                             index=0)
elif location_mode == "Custom Coordinates":
    custom_lat = st.sidebar.number_input(
        "📍 Latitude (°)",
        min_value=-90.0,
        max_value=90.0,
        value=45.0,
        help="Latitude in degrees (positive for North)")
    custom_lon = st.sidebar.number_input(
        "📍 Longitude (°)",
        min_value=-180.0,
        max_value=180.0,
        value=10.0,
        help="Longitude in degrees (positive for East)")
    custom_height = st.sidebar.number_input(
        "⛰️ Height (km)",
        min_value=0.0,
        max_value=10.0,
        value=0.5,
        help="Height above sea level in kilometers")

# Show preview map
st.markdown('<h2 class="sub-header">🗺️ Location Preview</h2>',
            unsafe_allow_html=True)

if location_mode == "Predefined City":
    preview_map = create_location_map(selected_city=selected_location)
    st.plotly_chart(preview_map, use_container_width=True)
elif location_mode == "Custom Coordinates":
    # Create map with custom location
    fig = go.Figure()
    fig.add_trace(
        go.Scattergeo(
            lon=[custom_lon],
            lat=[custom_lat],
            text=[
                f"Custom ({custom_lat}°N, {custom_lon}°E, {custom_height}km)"
            ],
            mode='markers+text',
            marker=dict(size=15, color='green', symbol='circle'),
            textposition="top center"))
    fig.update_geos(projection_type="natural earth",
                    showland=True,
                    landcolor="lightgray",
                    showocean=True,
                    oceancolor="lightblue",
                    showcountries=True,
                    countrycolor="white")
    fig.update_layout(title='Custom Location',
                      height=400,
                      margin=dict(l=0, r=0, t=50, b=0))
    st.plotly_chart(fig, use_container_width=True)
else:
    preview_map = create_location_map()
    st.plotly_chart(preview_map, use_container_width=True)

# Main content area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    calculate_button = st.button("🚀 Calculate Rain Attenuation",
                                 type="primary")

# Results display
if calculate_button:
    if location_mode == "Predefined City":
        # Single location calculation
        try:
            results = calc.calculate_for_location(frequency, polarization,
                                                  rain_rate, selected_location,
                                                  elevation_angle)

            # Display results
            st.markdown('<h2 class="sub-header">📊 Results</h2>',
                        unsafe_allow_html=True)

            # Key metrics
            metric_cols = st.columns(4)

            with metric_cols[0]:
                st.metric(label="🎯 Total Attenuation",
                          value=f"{results['A_R']:.4f} dB",
                          help="Total rain attenuation on the link")

            with metric_cols[1]:
                st.metric(label="⚡ Specific Attenuation",
                          value=f"{results['gamma']:.6f} dB/km",
                          help="Attenuation per kilometer of path")

            with metric_cols[2]:
                st.metric(label="📉 Reduction Factor",
                          value=f"{results['s']:.4f}",
                          help="Horizontal path reduction factor")

            with metric_cols[3]:
                st.metric(label="📏 Path Length",
                          value=f"{results['l_r']:.2f} km",
                          help="Slant path length through rain")

            # Additional details
            st.markdown('<h3 class="sub-header">🔍 Calculation Details</h3>',
                        unsafe_allow_html=True)

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
                """,
                            unsafe_allow_html=True)

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
                """,
                            unsafe_allow_html=True)

            # Sensitivity analysis charts
            st.markdown('<h3 class="sub-header">📈 Sensitivity Analysis</h3>',
                        unsafe_allow_html=True)

            chart_col1, chart_col2 = st.columns(2)

            with chart_col1:
                freq_chart = create_frequency_sensitivity_chart(
                    calc, selected_location, polarization, rain_rate,
                    elevation_angle)
                st.plotly_chart(freq_chart, use_container_width=True)

            with chart_col2:
                rain_chart = create_rain_rate_sensitivity_chart(
                    calc, selected_location, frequency, polarization,
                    elevation_angle)
                st.plotly_chart(rain_chart, use_container_width=True)

            # Export section for single location
            parameters = {
                "location": selected_location,
                "frequency_ghz": frequency,
                "polarization":
                "Vertical" if polarization == 'v' else "Horizontal",
                "rain_rate_mmh": rain_rate,
                "elevation_angle_deg": elevation_angle,
                "latitude": results['latitude'],
                "height_km": results['hs_km']
            }

            # Include sensitivity charts for export
            export_charts = {
                "Frequency Sensitivity": freq_chart,
                "Rain Rate Sensitivity": rain_chart
            }

            create_export_section(
                results, parameters,
                f"{selected_location.replace(' ', '_')}_results",
                export_charts)

        except Exception as e:
            st.error(f"❌ Error in calculation: {str(e)}")

    elif location_mode == "Custom Coordinates":
        # Custom coordinates calculation
        try:
            results = calc.calculate_rain_attenuation(frequency, polarization,
                                                      rain_rate, custom_lat,
                                                      custom_height,
                                                      elevation_angle)

            st.markdown(
                '<h2 class="sub-header">📊 Results for Custom Location</h2>',
                unsafe_allow_html=True)

            # Key metrics
            metric_cols = st.columns(4)

            with metric_cols[0]:
                st.metric(label="🎯 Total Attenuation",
                          value=f"{results['A_R']:.4f} dB",
                          help="Total rain attenuation on the link")

            with metric_cols[1]:
                st.metric(label="⚡ Specific Attenuation",
                          value=f"{results['gamma']:.6f} dB/km",
                          help="Attenuation per kilometer of path")

            with metric_cols[2]:
                st.metric(label="📉 Reduction Factor",
                          value=f"{results['s']:.4f}",
                          help="Horizontal path reduction factor")

            with metric_cols[3]:
                st.metric(label="📏 Path Length",
                          value=f"{results['l_r']:.2f} km",
                          help="Slant path length through rain")

            # Additional details
            details_col1, details_col2 = st.columns(2)

            with details_col1:
                st.markdown(f"""
                <div class="info-box">
                <h4>📍 Location Information</h4>
                <ul>
                    <li><strong>Latitude:</strong> {custom_lat:.1f}°</li>
                    <li><strong>Longitude:</strong> {custom_lon:.1f}°</li>
                    <li><strong>Height:</strong> {custom_height:.3f} km</li>
                    <li><strong>Rain Height:</strong> {results['h_r']:.3f} km</li>
                </ul>
                </div>
                """,
                            unsafe_allow_html=True)

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
                """,
                            unsafe_allow_html=True)

            # Export section for custom coordinates
            parameters = {
                "latitude": custom_lat,
                "longitude": custom_lon,
                "height_km": custom_height,
                "frequency_ghz": frequency,
                "polarization":
                "Vertical" if polarization == 'v' else "Horizontal",
                "rain_rate_mmh": rain_rate,
                "elevation_angle_deg": elevation_angle
            }
            create_export_section(results, parameters,
                                  f"custom_location_results")

        except Exception as e:
            st.error(f"❌ Error in calculation: {str(e)}")

    else:
        # All cities comparison
        try:
            all_results = calc.calculate_for_all_locations(
                frequency, polarization, rain_rate, elevation_angle)

            st.markdown('<h2 class="sub-header">🌍 Results for All Cities</h2>',
                        unsafe_allow_html=True)

            # Create comparison table
            comparison_data = []
            valid_results = {}

            for city, result in all_results.items():
                if 'error' not in result:
                    comparison_data.append({
                        'City':
                        city,
                        'Attenuation (dB)':
                        f"{result['A_R']:.4f}",
                        'Specific Attenuation (dB/km)':
                        f"{result['gamma']:.6f}",
                        'Reduction Factor':
                        f"{result['s']:.4f}",
                        'Path Length (km)':
                        f"{result['l_r']:.2f}",
                        'Rain Height (km)':
                        f"{result['h_r']:.3f}"
                    })
                    valid_results[city] = result

            if comparison_data:
                df_comparison = pd.DataFrame(comparison_data)
                st.dataframe(df_comparison, use_container_width=True)

                # Show map with results
                st.markdown('<h3 class="sub-header">🗺️ Attenuation Map</h3>',
                            unsafe_allow_html=True)
                results_map = create_location_map(all_results=valid_results,
                                                  show_all=True)
                st.plotly_chart(results_map, use_container_width=True)

                # Summary statistics
                st.markdown('<h3 class="sub-header">📈 Summary Statistics</h3>',
                            unsafe_allow_html=True)

                attenuations = [
                    result['A_R'] for result in valid_results.values()
                ]

                stat_cols = st.columns(4)

                with stat_cols[0]:
                    st.metric("📊 Average", f"{np.mean(attenuations):.4f} dB")

                with stat_cols[1]:
                    st.metric("📈 Maximum", f"{np.max(attenuations):.4f} dB")

                with stat_cols[2]:
                    st.metric("📉 Minimum", f"{np.min(attenuations):.4f} dB")

                with stat_cols[3]:
                    st.metric(
                        "📏 Range",
                        f"{np.max(attenuations) - np.min(attenuations):.4f} dB"
                    )

                # Bar chart comparison
                st.markdown(
                    '<h3 class="sub-header">📊 Attenuation Comparison</h3>',
                    unsafe_allow_html=True)

                cities = list(valid_results.keys())
                attenuations = [valid_results[city]['A_R'] for city in cities]

                fig_bar = go.Figure(data=[
                    go.Bar(x=cities, y=attenuations, marker_color='steelblue')
                ])

                fig_bar.update_layout(title='Rain Attenuation by City',
                                      xaxis_title='City',
                                      yaxis_title='Attenuation (dB)',
                                      height=400)

                st.plotly_chart(fig_bar, use_container_width=True)

                # Export section for all cities comparison
                parameters = {
                    "frequency_ghz": frequency,
                    "polarization":
                    "Vertical" if polarization == 'v' else "Horizontal",
                    "rain_rate_mmh": rain_rate,
                    "elevation_angle_deg": elevation_angle,
                    "cities_analyzed": len(comparison_data)
                }
                create_export_section(comparison_data, parameters,
                                      "all_cities_comparison")

            else:
                st.error("❌ No valid results obtained for any city")

        except Exception as e:
            st.error(f"❌ Error in calculations: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; margin-top: 2rem;">
    <p>🛰️ Rain Attenuation Calculator using ITU-R P.618 Model</p>
    <p>Developed for satellite communication link budget calculations</p>
</div>
""",
            unsafe_allow_html=True)
