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

def get_case_study_content3():
    st.subheader("State-wise Insurance transaction")
    statename_query = "select distinct State from aggregated_insurance"
    states = pd.read_sql(statename_query, connection)
    selected_state = st.selectbox("Select a State", states['State'])
    query1 = f"""select state,year,SUM(insurance_count) as total_insurance_count,SUM(insurance_amount) as total_insurance_amount
                    FROM phone_pe_pulse.aggregated_insurance
                    where state='{selected_state}'
                    group by state,year;"""
    df_result = pd.read_sql(query1, connection)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
                    x=df_result["year"],
                    y=df_result["total_insurance_count"],
                    mode='lines+markers',
                    name='Insurance Count'
                ))
    fig.add_trace(go.Scatter(
                    x=df_result["year"],
                    y=df_result["total_insurance_amount"],
                    mode='lines+markers',
                    name='Insurance Amount',
                    yaxis='y2'
                ))
    fig.update_layout(
                        title=f'Insurance Transactions Over Years in {selected_state}',
                        xaxis_title="Year",
                        yaxis=dict(title="Count"),
                        yaxis2=dict(title="Amount", overlaying='y', side='right')
                    )
    st.plotly_chart(fig)

    st.subheader("District-wise Insurance Amount trend")
    statename_query2 = "select distinct State from aggregated_insurance"
    states2 = pd.read_sql(statename_query2, connection)
    selected_state2 = st.selectbox("Select State", states2['State'])
    query2 = f"""select state,year,district,
                SUM(insurance_count) as Total_Insurance_Count,
                SUM(insurance_amount) as Total_Insurance_Amount
                FROM phone_pe_pulse.top_insurance_district
                where state='{selected_state2}'
                group by state,year,district;"""
    df_result = pd.read_sql(query2, connection)
    fig = px.scatter(
                    df_result,
                    x="year",
                    y="Total_Insurance_Amount",
                    size="Total_Insurance_Count",
                    color="district",
                    title="District-wise Insurance Amount Trend"
                )
    st.plotly_chart(fig)

    st.subheader("Average difference in transaction amount")
    statename_query3 = "select distinct State from aggregated_insurance"
    states3 = pd.read_sql(statename_query3, connection)
    selected_state3 = st.selectbox("State", states3['State'])
    query3 = f"""select year,current_amount,(current_amount-previous_value) as insurance_amount_change
                    from (
                    select year,SUM(insurance_amount) as current_amount,
                    LAG(SUM(insurance_amount),1,0) OVER (PARTITION BY state ORDER BY year) as previous_value
                    from aggregated_insurance 
                    where state='{selected_state3}'
                    group by year) t;"""
    df_result = pd.read_sql(query3, connection)
    fig = px.line(
                    df_result,
                    x="year",
                    y="insurance_amount_change",
                    markers=True,
                    title=f"Yearly Insurance amount difference (increase/decrease) for {selected_state3}"
                )
    st.plotly_chart(fig)

    st.subheader("State-wise Transaction count change (increase/decrease)")
    statename_query4 = "select distinct State from aggregated_insurance"
    states4 = pd.read_sql(statename_query4, connection)
    selected_state4 = st.selectbox("Choose State", states4['State'])
    query4 = f"""select year,current_count,
                    (current_count-previous_count) as insurance_count_change
                    from (
                    select year,SUM(insurance_count) as current_count,
                    LAG(SUM(insurance_count),1,0) OVER (PARTITION BY state ORDER BY year) as previous_count
                    from aggregated_insurance 
                    where state='{selected_state4}'
                    group by year) t;"""
    df_result = pd.read_sql(query4, connection)
    fig = px.bar(
                    df_result,
                    x="year",
                    y="insurance_count_change",
                    title=f"Yearly Insurance count difference (increase/decrease) for {selected_state4}"
                )
    st.plotly_chart(fig)

    st.subheader("Top 5 / Bottom 5 States based on Insurance Amount")
    query5 = """SELECT 
                    state,
                    SUM(insurance_amount) AS total_amount
                FROM aggregated_insurance
                GROUP BY state
                ORDER BY total_amount DESC;"""                            
    df_result = pd.read_sql(query5, connection)
    # Sort data
    df_sorted = df_result.sort_values(by="total_amount", ascending=False)
    # Top 5 and Bottom 5
    top5 = df_sorted.head(5)
    bottom5 = df_sorted.tail(5)
    df_combined = pd.concat([top5, bottom5])
    fig = px.funnel(
                        df_combined.sort_values(by='total_amount', ascending=False),
                        x='total_amount',
                        y='state',
                        color='state',
                        title='Funnel Chart - State Ranking by Insurance'
                    )
    st.plotly_chart(fig)