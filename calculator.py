import streamlit as st

st.title("Simple Calculator")
st.write("This is a simple calculator app built with Streamlit.")

c1,c2 = st.columns(2)

fnum = c1.number_input("Enter first number", value=0)
snum = c2.number_input("Enter second number", value=0)

options = ["Add", "Subtract", "Multiply", "Divide"]
choice = st.radio("Select operation", options)

button = st.button("Calculate")
result = 0
if button:
    if choice == 'Add':
        result = fnum + snum
    if choice == 'Subtract':
        result = fnum - snum
    if choice == 'Multiply':
        result = fnum * snum
    if choice == 'Divide':
        result = fnum / snum
st.success(f"The result is: {result}")
       