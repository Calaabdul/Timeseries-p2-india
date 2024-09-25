#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:01:06 2024

@author: dr.u.aajidagba
"""


import streamlit as st
import pickle

#load saved model
with open('models/arima.pkl', 'rb') as file:
    best_model = pickle.load(file)
    
    
st.title('P2.5 Reading Prediction App')
  
#input variables 
def input():
    #number of future steps for prediction
    steps = st.number_input('Enter the number of future steps to predict:' , min_value =1, value = 3)
    return steps
    
steps = input()   
 
 
#prediction     
def make_prediction():
    result = best_model.forecast(steps = steps)
    return result()
    
#prediciton button    
if st.button('Predict'):
    result = make_prediction()
    st.write(f'Predicted P2.5 readings for the next {steps} steps:')
    st.write(result)
    