import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def calculator():
    st.title("Calculator App")
    st.header("Muhammad Taha")

    num1 = st.number_input("Enter the first number:", format="%.2f")
    operator = st.selectbox("Select the operator", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter the second number:", format="%.2f")

    if st.button("Calculate"):
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator. Please try again."

        st.write("Result:", result)

    if st.button("Quit Calculator"):
        st.write("Goodbye!")

if __name__ == "__main__":
    calculator()
