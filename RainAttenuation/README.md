# 🌧️ Rain Attenuation Calculator

A comprehensive implementation of the ITU-R P.618 model for calculating rain attenuation in satellite communication links.

## 📁 Project Structure

```
RainAttenuation/
├── README.md                           # This file - project overview and usage
├── rain_attenuation_notebook.ipynb    # Interactive Jupyter notebook with widgets
└── RainAttenuationWebApp/              # Web application directory
    ├── app.py                          # Streamlit web dashboard
    ├── rain_attenuation_core.py        # Core calculation engine (CLI + API)
    └── requirements.txt                # Python dependencies
```

##  Which File to Use?

### 📊 **For Interactive Exploration** → `rain_attenuation_notebook.ipynb`
- **Best for**: Learning, research, parameter exploration
- **Features**: Interactive widgets, inline plots, step-by-step calculations
- **Run with**: `jupyter notebook rain_attenuation_notebook.ipynb`

### 🌐 **For Beautiful Web Interface** → `RainAttenuationWebApp/app.py`
- **Best for**: Presentations, client demos, comprehensive analysis
- **Features**: Interactive maps, multiple visualizations, professional UI
- **Run locally**: Navigate to the directory with cd `RainAttenuationWebApp` and launch via `streamlit run app.py` (requires Streamlit installed: `pip install streamlit`).
- **OR**: Visit the hosted Streamlit dashboard (built using the same principles as the notebook): https://rainattenuation.streamlit.app/

### ⚙️ **For Integration & Automation** → `RainAttenuationWebApp/rain_attenuation_core.py`
- **Best for**: Scripts, automation, integration into other projects
- **Features**: Command-line interface, importable classes, batch processing
- **Run with**: `cd RainAttenuationWebApp && python rain_attenuation_core.py [options]`

## Quick Start

### 1. **Install Dependencies**
```bash
cd RainAttenuationWebApp
pip install -r requirements.txt
```

### 2. **Run the Web Dashboard**
```bash
cd RainAttenuationWebApp
streamlit run app.py
```

### 3. **Try Command Line Examples**
```bash
cd RainAttenuationWebApp

# Single location calculation
python rain_attenuation_core.py -f 2.5 -p v -r 30 -l Madrid -e 15 -v

# All locations with plot
python rain_attenuation_core.py -f 2.0 -p v -r 30 -e 30 --all-locations --plot

# Custom coordinates
python rain_attenuation_core.py -f 3.0 -p h -r 50 --lat 45.0 --height 0.5 -e 20 -v
```

### 4. **Import into Your Code**
```python
import sys
sys.path.append('RainAttenuationWebApp')
from rain_attenuation_core import RainAttenuationCalculator

calc = RainAttenuationCalculator()
results = calc.calculate_for_location(2.5, 'v', 30, 'Madrid', 15)
print(f"Attenuation: {results['A_R']:.4f} dB")
```

## Features

### **Core Calculations**
- ✅ ITU-R P.618 compliant implementation
- ✅ Frequency range: 1-4 GHz
- ✅ Both horizontal and vertical polarization
- ✅ Linear interpolation for intermediate frequencies
- ✅ Comprehensive input validation

### **Location Support**
- ✅ 10 predefined European cities
- ✅ Custom latitude/longitude coordinates
- ✅ Height above sea level consideration
- ✅ Interactive world maps with pins

### **Visualizations**
- ✅ Interactive bar charts (Plotly)
- ✅ Geographic scatter plots
- ✅ Attenuation vs latitude analysis
- ✅ Text-based plots (no dependencies)
- ✅ Summary statistics

### **User Interfaces**
- ✅ Jupyter notebook with widgets
- ✅ Streamlit web dashboard
- ✅ Command-line interface
- ✅ Python API for integration

## ITU-R P.618 Model Parameters

| Parameter | Description | Range | Units |
|-----------|-------------|-------|-------|
| **f** | Frequency | 1.0 - 4.0 | GHz |
| **pol** | Polarization | h, v | - |
| **R** | Rain rate | ≥ 0 | mm/h |
| **φ** | Latitude | -90 to 90 | degrees |
| **hs** | Height above sea level | ≥ 0 | km |
| **ε₀** | Elevation angle | 1 - 90 | degrees |

## Predefined Locations

| City | Latitude | Height | City | Latitude | Height |
|------|----------|--------|------|----------|--------|
| Madrid | 40.4°N | 588m | Vienna | 48.2°N | 193m |
| Tirana | 41.3°N | 104m | Paris | 48.8°N | 34m |
| Rome | 41.9°N | 14m | Brussels | 50.8°N | 76m |
| Pristina | 42.6°N | 652m | London | 51.5°N | 14m |
| Zagreb | 45.8°N | 130m | Berlin | 52.5°N | 34m |

## Example Use Cases

### 🛰️ **Satellite Link Design**
Calculate rain margins for your satellite communication system:
```python
# Design a link for Madrid with 99.99% availability
results = calc.calculate_for_location(12.0, 'v', 30, 'Madrid', 45)
link_margin = results['A_R'] + 3  # Add 3dB safety margin
```

### 🌍 **Site Comparison**
Compare multiple locations for optimal satellite ground station placement.

### 📊 **Parameter Studies**
Analyze the impact of frequency, elevation angle, and location on attenuation.

### 🔬 **Research & Education**
Validate ITU-R P.618 model predictions against measurements.

## 🔧 Advanced Usage

### **Batch Processing**
```python
calc = RainAttenuationCalculator()
frequencies = [1.5, 2.0, 2.5, 3.0, 3.5]
results = {}

for freq in frequencies:
    results[freq] = calc.calculate_all_locations(freq, 'v', 30, 15)
```

### **Custom Analysis**
```python
# Analyze elevation angle sensitivity
elevations = range(5, 91, 5)
madrid_results = []

for elev in elevations:
    result = calc.calculate_for_location(2.5, 'v', 30, 'Madrid', elev)
    madrid_results.append((elev, result['A_R']))
```

## ⚠️ Important Notes

- **Rain Rate**: Use the rain rate exceeded for 0.01% of an average year
- **Frequency Limits**: Model is valid for 1-4 GHz
- **Elevation Angles**: Very low angles may give unrealistic results
- **Geographic Scope**: Predefined locations are European cities

## 🛠️ Development

### **Project History**
1. ✅ Optimized original Jupyter notebook for efficiency
2. ✅ Created standalone Python module with CLI
3. ✅ Built interactive Streamlit web dashboard with maps
4. ✅ Added comprehensive documentation and examples

### **File Dependencies**
- `RainAttenuationWebApp/app.py` imports `rain_attenuation_core.py`
- `rain_attenuation_notebook.ipynb` is standalone
- All files use the same coefficient tables and algorithms

### **Contributing**
This project implements the ITU-R P.618 standard. Any modifications should maintain compliance with the recommendation.

## 📄 References

- **ITU-R P.618**: Propagation data and prediction methods required for the design of Earth-space telecommunication systems
- **Table 2.1**: Regression coefficients for specific attenuation
- **Table 2.5**: European city coordinates and heights

---

*Built with Python, Streamlit, Plotly, and Jupyter • ITU-R P.618 Compliant*