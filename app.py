import pickle
import streamlit as st
import pandas as pd
import numpy as np

#load model
with open('car_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

from os import curdir
#streamlit app UI
st.title("Car Price Prediction App")
st.markdown("Enter specifications to predict the price")

#Input fields for selected features
carwidth = st.number_input("Car Width (inches)", min_value=5.0, max_value=80.0, value=65.0)
curbweight = st.number_input("Curb Weight (kgs)", min_value=500.0, max_value=2000.0, value=1200.0)
enginesize = st.number_input("Engine Size (cc)", min_value=60.0, max_value=400.0, value=150.0)
boreratio = st.number_input("Bore Ratio", min_value=2.0, max_value=5.0, value=3.2)
rotor = st.selectbox("Has Rotor Brakes?", [0, 1])
three = st.selectbox("Three Cylinder Engine?", [0, 1])
Highend = st.selectbox("Is Highend Brand?", [0, 1])
bmw = st.selectbox("Is BMW?", [0, 1])
rear = st.selectbox("Rear Wheel Drive?", [0, 1])

# Create input dataframe
input_data = pd.DataFrame({
    'carwidth': [carwidth],
    'curbweight': [curbweight],
    'enginesize': [enginesize],
    'boreratio': [boreratio],
    'rotor': [rotor],
    'three': [three],
    'Highend': [Highend],
    'bmw': [bmw],
    'rear': [rear]
})

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Car Price: ₹{prediction:,.2f}")
