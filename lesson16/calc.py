import streamlit as st

def calculate(num1, num2, operation ):
    if operation == "addition":
        result = num1 + num2
    elif operation == "subtraction":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = ("number could not be divided")
    return result

def main():
    st.title = ("SIMPLE CALC")
    num1 = st.number_input("type the first number that comes to mind", step=1)
    num2 = st.number_input("type the second number that comes to mind ", step=2)
    operation = st.radio("select operation", ['addition', 'subtraction', 'multiply', 'divide'])

    result = calculate(num1, num2, operation)

    st.write(f"rsult of {operation} of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()