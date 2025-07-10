
# Fundamentals #
import streamlit as st 

def bmi_app():
    st.write('BMI Calculator')
    height = st.number_input("Enter the height (meter)",min_value=1,max_value=20) 
    weight = st.number_input("Enter the weight(Kg)",min_value=20,max_value=100) 

    # if height == None:
    #     st.error("Height is Mendatory")
    # if weight == None:
    #     st.error("weight is Mendatory")  
    # Add Button 

    button = st.button('Calculate BMI')
    if button:
        bmi = weight/(height**2)
        st.success(f"Your BMI is {bmi}")
