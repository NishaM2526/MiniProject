import streamlit as st
from RevenuePrediction import get_revenue_prediction_content

st.set_page_config(page_title="Youtube Monetization")
st.markdown("""
    <style>
           .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 3rem;
                padding-right: 3rem;
            }
    </style>
    """, unsafe_allow_html=True)
st.title("YouTube Monetization Analysis", text_alignment="center")
st.markdown("""
<style>
h3 {
    font-size: 25px !important;
}
</style>
""", unsafe_allow_html=True)

st.write("To determine if your YouTube channel can be monetized, we need to analyze several key metrics. " \
    "Please provide the following information about your channel and videos:")
with st.form(key="monetization_form"):
    st.subheader("Subscriber count")
    col1, col2 = st.columns(2)
    with col1:
        subscribers = st.number_input("Subscriber count", min_value=0, value=0, step=1,label_visibility="collapsed")

    st.subheader("Details about your Video")
    col1, col2 = st.columns(2)
    with col1:
        category_map = {"Education": 0, "Entertainment": 1, "Gaming": 2, "Lifestyle": 3, "Music": 4, "Technology": 5}
        category = st.selectbox("Video category", options=list(category_map.keys()))
        numeric_value = category_map[category]
    with col2:
        video_length = st.slider("Video Length in minutes", 0, 60, 15)

    col1, col2 = st.columns(2)
    with col1:
        watch_time = st.number_input("Expected Overall Watch Time in minutes", min_value=0, value=60, step=1)

    col1, col2,col3 = st.columns(3)
    with col1:
        views = st.number_input("Expected Views count", min_value=0, value=0, step=1)
    with col2:
        likes = st.number_input("Expected Likes count", min_value=0, value=0, step=1)
    with col3:
        comments = st.number_input("Expected Comments count", min_value=0, value=0, step=1)

    submit_button = st.form_submit_button(label='Predict Monetization Potential', use_container_width=True, type="primary")

if submit_button:
    user_inputs = {
        "subscribers": subscribers,
        "category": numeric_value,
        "video_length": video_length,
        "watch_time": watch_time,
        "views": views,
        "likes": likes,
        "comments": comments
    }
    get_revenue_prediction_content(self=None, input_data=user_inputs)