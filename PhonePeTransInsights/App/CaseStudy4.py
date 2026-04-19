import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import mysql.connector

# SQL connection
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    password="Nisha@2506",
    database="phone_pe_pulse"
)
cursor = connection.cursor()

def get_case_study_content4():
    st.subheader("Top-performing Districts in terms of transaction value")
    statename_query = "select distinct State from top_transaction_district"
    states = pd.read_sql(statename_query, connection)
    selected_states = st.selectbox("Select a State", states['State'])
    query1 = f"""select year,state,district,trans_amount from (
                    select 
                        year,
                        state,
                    district,
                        SUM(transaction_amount) AS trans_amount,
                        RANK() over (partition by year order by SUM(transaction_amount) desc) as rnk
                    FROM top_transaction_district
                    where state='{selected_states}'
                    GROUP BY year,state,district) t where rnk=1;"""
    df_result = pd.read_sql(query1, connection)
    fig = px.bar(df_result, x='year', y='trans_amount',color='district',
                 title='Top District by Transaction Amount each Year')
    st.plotly_chart(fig)

    st.subheader("Top-performing Pincodes in terms of transaction value")
    statename_query2 = "select distinct State from top_transaction_pincode"
    states2 = pd.read_sql(statename_query2, connection)
    selected_states2 = st.selectbox("Select State", states2['State'])
    query2 = f"""select year,state,pincode,total_value from (
                    select 
                        year,
                        state,
                        pincode,
                        SUM(transaction_amount) AS total_value,
                        RANK() over (partition by year order by SUM(transaction_amount) desc) as rnk
                    FROM top_transaction_pincode
                    where state='{selected_states2}'
                    GROUP BY year,state, pincode) t where rnk=1;"""
    df_result = pd.read_sql(query2, connection)
    fig = px.strip(
                    df_result,
                    x='year',
                    y='total_value',
                    color='pincode',
                    title='Strip chart ofTop Pincodes by Transaction Amount each Year'
                )
    st.plotly_chart(fig)

    st.subheader("Top districts by average transaction")
    statename_query3 = "select distinct State from top_transaction_district"
    states3 = pd.read_sql(statename_query3, connection)
    selected_states3 = st.selectbox("State", states3['State'])
    query3 = f"""SELECT 
                        state,
                        district,
                        SUM(transaction_amount) / NULLIF(SUM(transaction_count), 0) AS avg_transaction
                    FROM top_transaction_district
                    where state='{selected_states3}'
                    GROUP BY state, district
                    ORDER BY avg_transaction desc;"""
    df_result = pd.read_sql(query3, connection)
    fig = px.bar(df_result, x='district', y='avg_transaction',color='district',
                 title='Top District by Average Transaction')
    st.plotly_chart(fig)

    st.subheader("Top vs Bottom States by Transaction Volume")
    year_query4 = "select distinct year from top_transaction_pincode"
    years4 = pd.read_sql(year_query4, connection)
    selected_year4 = st.selectbox("Select a Year", years4['year'])
    query4 = f"""select year,state,sum(transaction_count) as transaction_volume,
                    RANK() over (order by sum(transaction_count) desc) as rnk
                    from top_transaction_pincode
                    where year='{selected_year4}'
                    group by state,year;"""
    df_result = pd.read_sql(query4, connection)
    top10 = df_result.head(5)
    bottom10 = df_result.tail(5)
    combined = pd.concat([top10, bottom10])
    combined['Category'] = ['Top']*5 + ['Bottom']*5
    fig = px.funnel(
                        combined.sort_values(by='transaction_volume', ascending=False),
                        x='transaction_volume',
                        y='state',
                        color='Category',
                        title='State Ranking by Transaction Volume',
                        color_discrete_map={
                                                'Top': 'green',
                                                'Bottom': 'red'
                                            }
                    )
    st.plotly_chart(fig)

    st.subheader("Top Performed States Yearly")
    query5 = """select year as Year,state as State,transaction_value as Transaction_Value from (
                    select year,state,sum(transaction_amount) as transaction_value,
                    RANK() over (partition by year order by sum(transaction_amount) desc) as rnk
                    from top_transaction_district
                    group by state,year)t where rnk=1;"""
    df_result = pd.read_sql(query5, connection)
    row_colors = ['#f9f9f9', '#e6f2ff'] * (len(df_result)//2 + 1)

    fig = go.Figure(data=[go.Table(    
                                    # Header styling
                                    header=dict(
                                        values=list(df_result.columns),
                                        fill_color='#1f4e79',
                                        font=dict(color='white', size=14, family='Arial'),
                                        align='center',
                                        height=35
                                    ),
    
                                    # Cell styling
                                    cells=dict(
                                        values=[df_result[col] for col in df_result.columns],
                                        fill_color=[row_colors],
                                        font=dict(color='black', size=18, family='Arial'),
                                        align=['center', 'left', 'right'],  # column-wise alignment
                                        height=30
                                    )
                                )])     

    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=10)
    )
    
    st.plotly_chart(fig)