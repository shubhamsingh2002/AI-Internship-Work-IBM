import pandas
import joblib as  jl

import streamlit as st

# model = jl.load('mj')


st.title('house prediction')

# def prediction (area):
#     prediction = model.predict([[area]])
#     return prediction


area = st.number_input("Area")


def prediction(area):
    # p = model.predicy([[area]])
    return p 



st.button("Predict")

if(st.button("Predict")):
    result = prediction(area)
    st.success("The predicted price is {}".format(result))