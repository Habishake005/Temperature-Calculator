import streamlit as st

st.title("🌡 Temperature Converter App")

st.write("Enter temperature in Celsius to convert to Fahrenheit")

celsius = st.number_input("Enter Temperature (°C):")

if st.button("Convert"):
    fahrenheit = (celsius * 9/5) + 32
    st.success(f"The converted temperature is {fahrenheit:.2f} °F")
