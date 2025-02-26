import streamlit as st
from pint import UnitRegistry

# Initialize UnitRegistry
ureg = UnitRegistry()

# Define unit categories and units
unit_categories = {
    "Length": {
        "units": ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter", "millimeter"],
        "formula": "multiply the length value by {factor}"
    },
    "Weight": {
        "units": ["gram", "kilogram", "pound", "ounce"],
        "formula": "multiply the weight value by {factor}"
    },
    "Temperature": {
        "units": ["celsius", "fahrenheit", "kelvin"],
        "formula": "temperature conversion uses a formula"
    },
    "Time": {
        "units": ["second", "minute", "hour", "day"],
        "formula": "multiply the time value by {factor}"
    },
    "Speed": {
        "units": ["meter/second", "kilometer/hour", "mile/hour"],
        "formula": "multiply the speed value by {factor}"
    },
}

# Streamlit UI
st.title("🌍 Google-Style Unit Converter")

# Select category
category = st.selectbox("Select a category:", list(unit_categories.keys()))

# Select from & to units
units = unit_categories[category]["units"]
from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)

# User input
value = st.number_input("Enter value:", min_value=0.0, format="%.4f")

# Perform conversion
if st.button("Convert"):
    try:
        # Handle temperature separately
        if category == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
                formula = "C × 9/5 + 32"
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
                formula = "(F - 32) × 5/9"
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
                formula = "C + 273.15"
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
                formula = "K - 273.15"
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
                formula = "(F - 32) × 5/9 + 273.15"
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
                formula = "(K - 273.15) × 9/5 + 32"
            else:
                result = value
                formula = "Same unit"

        else:
            # Perform general conversion using Pint
            converted = (value * ureg(from_unit)).to(to_unit)
            result = converted.magnitude
            factor = converted.magnitude / value if value != 0 else 1
            formula = unit_categories[category]["formula"].format(factor=round(factor, 4))

        # Display Result
        st.markdown(f"""
            <div style="border:1px solid #ddd; padding:10px; border-radius:5px; text-align:center; font-size:24px;">
                <b>{value} {from_unit}</b> = <b>{result:.4f} {to_unit}</b>
            </div>
        """, unsafe_allow_html=True)

        # Show formula
        st.markdown(f"""<div style="background:#f7f7f7; padding:5px; border-radius:5px; color:#444;">
            <b style="background:#FFCC00; padding:3px 5px; border-radius:3px;">Formula</b>
            <span style="font-size:16px;"> {formula}</span>
        </div>""", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Pint by [Sadiq Khan](https://github.com/sadiqkhan7777)")
