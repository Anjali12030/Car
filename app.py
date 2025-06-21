import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np
import pickle as pkl
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


#load model 
with open('car_price.pkl','rb') as file:
    model = pkl.load(file)

# streamlit app UI
st.title("Car Price Prediction App")
st.markdown("Enter car Specification to predict the price")

# input fields for selected features
carwidth = st.number_input("car width(inches)", min_value= 50.0 , max_value = 80.0, value = 65.0)
curbweight = st.number_input("Curb weight (kg)",min_value=500.0,max_value=2000.0 , value = 1200.0)
enginesize = st.number_input("Engine Size (cc)",min_value=60.0, max_value=400.0,value=150.0)
boreratio = st.number_input("Bore Ratio",min_value=2.0,max_value=5.0,value = 3.2)
rotor = st.selectbox("Has Rotor Brakes?",[0,1])
three = st.selectbox("Three Cylinder Engine ?",[0,1])
Highend = st.selectbox("Is Highend Brand?",[0,1])
bmw = st.selectbox("is BMW ?",[0,1])
rear = st.selectbox("Rear Wheel Drive?",[0,1])


# create input Dataframe
input_data = pd.DataFrame({
    'carwidth':[carwidth],
    'curbweight':[curbweight],
    'enginesize':[enginesize],
    'boreratio' :[boreratio],
    'rotor':[rotor],
    'three':[three],
    'Highend':[Highend],
    'bmw':[bmw],
    'rear':[rear]})


# Prediction

if st.button("prediction price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Car price: Rs.{prediction[0]:,.2f}")
