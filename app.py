import streamlit as st
from predict_page import show_predict_page  
from visualize import show_visualization

with st.sidebar:
    op_win=st.selectbox("Predict or Visualize",["Predict","Visualize"])

if op_win=="Predict":
    show_predict_page()

if op_win=="Visualize":
    show_visualization()
    