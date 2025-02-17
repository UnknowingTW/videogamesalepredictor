import streamlit as st
import numpy as np
import joblib

#Interface
st.markdown('## Video game Sales Prediction')

year = st.number_input('year(number)')
NA_Sales = st.number_input('NA_Sales(number)')
EU_Sales = st.number_input('EU_Sales(number)')
JP_Sales = st.number_input('JP_Sales(number)')
Other_Sales = st.number_input('Other_Sales(number)')

# Predict button
if st.button('Predict'):
    model = joblib.load('model.pk1')
    X = np.array([year, NA_Sales, EU_Sales, JP_Sales, Other_Sales]).reshape(1, -1)
    
    # Check if any value in X is <= 0
    if np.any(X <= 0):
        st.markdown('### Inputs must be greater than 0')
    else:
        prediction = model.predict(X)[0]
        st.markdown(f'### Prediction is {prediction}')
        