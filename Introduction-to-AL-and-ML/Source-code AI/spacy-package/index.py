# Running Script of Streamlit

import streamlit as st
from app.hello import hello_app 
from app.bmi import bmi_app 
    
st.title("Index Application")
# hello_app() 

bmi_app()
