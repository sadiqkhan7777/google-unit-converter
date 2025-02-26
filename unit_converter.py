import streamlit as st

def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 0.001,
        'milligrams': 0.000001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic meters': 1000,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.24
    }
    return value * volume_units[from_unit] / volume_units[to_unit]

def main():
    st.title("Unit Converter")
    
    # Conversion type selection
    conversion_type = st.selectbox(
        "Select conversion type",
        ["Length", "Weight", "Temperature", "Volume"]
    )
    
    # Input value
    value = st.number_input("Enter value to convert", min_value=0.0, value=1.0)
    
    # Unit selection based on conversion type
    if conversion_type == "Length":
        units = ['meters', 'kilometers', 'centimeters', 'millimeters', 
                'miles', 'yards', 'feet', 'inches']
        from_unit = st.selectbox("From unit", units)
        to_unit = st.selectbox("To unit", units)
        if st.button("Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
            
    elif conversion_type == "Weight":
        units = ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces']
        from_unit = st.selectbox("From unit", units)
        to_unit = st.selectbox("To unit", units)
        if st.button("Convert"):
            result = convert_weight(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
            
    elif conversion_type == "Temperature":
        units = ['celsius', 'fahrenheit', 'kelvin']
        from_unit = st.selectbox("From unit", units)
        to_unit = st.selectbox("To unit", units)
        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
            
    elif conversion_type == "Volume":
        units = ['liters', 'milliliters', 'cubic meters', 'gallons', 
                'quarts', 'pints', 'cups']
        from_unit = st.selectbox("From unit", units)
        to_unit = st.selectbox("To unit", units)
        if st.button("Convert"):
            result = convert_volume(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
