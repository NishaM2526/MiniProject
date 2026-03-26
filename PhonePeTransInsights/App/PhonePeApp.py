import streamlit as st
import Indiamap as imap
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import mysql.connector

from CaseStudy1 import get_case_study_content
from CaseStudy2 import get_case_study_content2
from CaseStudy3 import get_case_study_content3
from CaseStudy4 import get_case_study_content4

# SQL connection
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    password="Nisha@2506",
    database="phone_pe_pulse"
)
cursor = connection.cursor()

st.set_page_config(page_title="PhonePe Pulse")
st.sidebar.title("Navigation")
navigation_bar = st.sidebar.selectbox("Select a page", ["Home", "Analysis"])  

if navigation_bar == "Home":
    fig = imap.load_map() 
    st.subheader("PhonePe Transaction Insights - 2024")   
    st.plotly_chart(fig)

elif navigation_bar == "Analysis":
    st.title("Business Case Study")
    casestudy = st.selectbox("Choose Case Study", 
                         ["Decoding Transaction Dynamics on PhonePe", 
                          "Device Dominance and User Engagement Analysis",
                          "Insurance Penetration and Growth Potential Analysis",
                          "Transaction Analysis Across States and Districts Scenario",
                          "User Registration Analysis"
                         ]
                        ) 
    if casestudy == "Decoding Transaction Dynamics on PhonePe":        
        get_case_study_content()         
    elif casestudy == "Device Dominance and User Engagement Analysis":
        get_case_study_content2()   
    elif casestudy == "Insurance Penetration and Growth Potential Analysis":
        get_case_study_content3()   
    elif casestudy == "Transaction Analysis Across States and Districts Scenario":  
        get_case_study_content4()          

cursor.close()
connection.close()