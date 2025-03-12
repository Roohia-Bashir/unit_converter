import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Load external CSS file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Extended unit conversion dictionary
unit_dict = {
    "Length": {
        "meter": 1, "centimeter": 0.01, "kilometer": 1000, "millimeter": 0.001,
        "inch": 0.0254, "foot": 0.3048, "yard": 0.9144, "mile": 1609.344,
        "nautical mile": 1852
    },
    "Area": {
        "square meter": 1, "square kilometer": 1e6, "square centimeter": 0.0001,
        "square mile": 2.58999e6, "square foot": 0.092903, "square inch": 0.00064516,
        "hectare": 10000, "acre": 4046.86
    },
    "Volume": {
        "cubic meter": 1, "liter": 0.001, "milliliter": 1e-6,
        "gallon": 0.00378541, "cubic foot": 0.0283168, "cubic inch": 0.0000163871
    },
    "Mass": {
        "kilogram": 1, "gram": 0.001, "milligram": 1e-6, "metric ton": 1000,
        "pound": 0.453592, "ounce": 0.0283495, "stone": 6.35029
    },
    "Temperature": {
        "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
    },
    "Speed": {
        "meters per second": 1, "kilometers per hour": 0.277778,
        "miles per hour": 0.44704, "knots": 0.514444
    },
    "Time": {
        "second": 1, "minute": 60, "hour": 3600, "day": 86400,
        "week": 604800, "month": 2.592e6, "year": 3.154e7
    },
    "Pressure": {
        "pascal": 1, "kilopascal": 1000, "bar": 1e5,
        "psi": 6894.76, "atmosphere": 101325
    },
    "Energy": {
        "joule": 1, "kilojoule": 1000, "calorie": 4.184,
        "kilocalorie": 4184, "watt hour": 3600, "kilowatt hour": 3.6e6
    }
}

# Function for unit conversion
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    
    from_factor = unit_dict[category][from_unit]
    to_factor = unit_dict[category][to_unit]
    return (value * from_factor) / to_factor

# Function for temperature conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

# Add custom class to title for specific styling
st.markdown("<div class='app-header'><h1 class='converter-title'>🔄 Unit Converter</h1></div>", unsafe_allow_html=True)

# Main container for better styling
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Select category with icon
st.markdown("<div class='section-label'><span class='icon'>📊</span> Select Category</div>", unsafe_allow_html=True)
category = st.selectbox("Select a category:", list(unit_dict.keys()), label_visibility="collapsed")

# Create columns for unit selection
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='section-label'><span class='icon'>📥</span> From Unit</div>", unsafe_allow_html=True)
    units = list(unit_dict[category].keys())
    from_unit = st.selectbox("From Unit:", units, label_visibility="collapsed")

with col2:
    st.markdown("<div class='section-label'><span class='icon'>📤</span> To Unit</div>", unsafe_allow_html=True)
    to_unit = st.selectbox("To Unit:", units, label_visibility="collapsed")

# Input value with proper formatting
st.markdown("<div class='section-label'><span class='icon'>🔢</span> Enter Value</div>", unsafe_allow_html=True)

# Use a workaround for the number input styling
col_val1, col_val2 = st.columns([3, 1])
with col_val1:
    value = st.number_input("Enter value:", value=1.0, step=0.1, format="%.4f", label_visibility="collapsed")

# Convert button with better UI
if st.button("Convert", use_container_width=True):
    result = convert_units(value, from_unit, to_unit, category)
    st.markdown(f"<div class='result-card'><div class='result-icon'>✨</div><div class='result-content'><div class='result-label'>Result</div><div class='result-value'>{result:.6g} {to_unit}</div></div></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close main container

# Footer
st.markdown("<div class='footer'>© 2025 Unit Converter | Developed by Roohia Bashir</div>", unsafe_allow_html=True)
