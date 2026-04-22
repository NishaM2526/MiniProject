
import os
from joblib import Parallel, delayed
import joblib
import streamlit as st  
import numpy as np 

base_dir = os.path.dirname(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
file_path = os.path.join(base_dir, "Data", "linear_regression_model.pkl")

def get_revenue_prediction_content(self, input_data):
    model = joblib.load(file_path)    
    
    views = input_data['views']
    likes = input_data['likes']
    comments = input_data['comments']
    watch_time = float(input_data['watch_time'])
    video_length = float(input_data['video_length'])
    subscribers = input_data['subscribers']
    category = input_data['category']
    if input_data['views'] != 0:
        engagement_rate = (input_data['likes'] + input_data['comments']) / input_data['views']
    else:
        engagement_rate = 0
    input_value = np.array([[views, likes, comments, watch_time, video_length, subscribers, category, engagement_rate]])
    prediction = model.predict(input_value)

    st.markdown(f"## Predicted Ad Revenue : :red[~${prediction[0]:.2f} USD]",unsafe_allow_html=True)
    
 
    

