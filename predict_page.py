import pickle
import streamlit as st
import numpy as np
import pandas as pd
import sklearn

education=['Bachelor’s degree', 'Less than a Bachelors', 'Master’s degree', 'Post grad']
country=['Australia' ,'Brazil' ,'Canada' ,'Denmark' ,'France' ,'Germany' ,'India',
 'Israel' ,'Italy' ,'Netherlands' ,'Norway' ,'Poland' ,'Spain' ,'Sweden',
 'Switzerland' ,'United Kingdom of Great Britain and Northern Ireland',
 'United States of America']

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()



regressor_loaded = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Engineer Salary Prediction")
    st.write("## Provide the inputs ##")
    input_country=st.selectbox("Country",country)
    input_edu=st.selectbox("Education Level",education)
    input_exp=st.slider("Work Experience",0,50)

    if st.button("Predict Salary"):
        X = np.array([[input_country, input_edu,input_exp]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        salary = regressor_loaded.predict(X)

        # Assuming salary is an array and you want to display the first value
        st.subheader(f"Estimated Salary is ${salary[0]:,.2f}")


