import streamlit as st

def calculate(name, height, age):
    result = height / age
    st.write(f"Division result: {result}")

    if result > 11:
        st.success(f"{name} makes the team")
    else:
        st.error(f"{name} does not make the team")

# Input fields
name = st.text_input("Your name")
height = st.number_input("Your height in cm (e.g., 190)", min_value=1, step=1)  # Whole number input
age = st.number_input("Your age", min_value=0, step=1)  # Whole number input

# Check button
if st.button("Check"):
    if name and height and age:
        calculate(name, height, age)
    else:
        st.warning("Please fill out all the fields.")
