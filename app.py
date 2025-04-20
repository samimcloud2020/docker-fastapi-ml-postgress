import streamlit as st
from main import model



st.title("House Price Predictor")
st.write("Enter the area and number of rooms to predict the price of a house.")

area = st.number_input("Area (sq ft)", min_value=100, step=50)
room = st.number_input("Number of Rooms", min_value=1, step=1)

if st.button("Predict"):
    features = [[area, room]]
    prediction = model.predict(features)
    st.success(f"Estimated Price: {prediction[0]:,.2f}")
