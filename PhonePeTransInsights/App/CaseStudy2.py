import streamlit as st
import plotly.express as px
import pandas as pd
import mysql.connector

# SQL connection
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    password="Nisha@2506",
    database="phone_pe_pulse"
)
cursor = connection.cursor()

def get_case_study_content2():
    st.subheader("Device brands usage across states")
    col1, col2 = st.columns(2)
    statename_query = "select distinct State from aggregated_users"
    year_query = "select distinct year from aggregated_users"
    states = pd.read_sql(statename_query, connection)
    years = pd.read_sql(year_query, connection)
    with col1:
        selected_state = st.selectbox("Select a State", states['State'])
    with col2:
        selected_year = st.selectbox("Select a Year", years['year'])
    query1 = f"""select user_brand,sum(user_count) as user_count
                FROM phone_pe_pulse.aggregated_users
                where state='{selected_state}' and year='{selected_year}'
                group by user_brand"""
    df_result = pd.read_sql(query1, connection)
    fig = px.bar(df_result, x='user_brand', y='user_count',color='user_brand',
                 title=f'User Count by Device Brand in {selected_state} for {selected_year}')
    st.plotly_chart(fig)

    st.subheader("State-wise - Registered users & app opens")
    statename_query2 = "select distinct State from aggregated_users"
    states2 = pd.read_sql(statename_query2, connection)
    selected_state2 = st.selectbox("Select State", states2['State'])
    query2 = f"""select year,sum(registered_user) as registered_users,sum(app_opens) as app_opens
                from phone_pe_pulse.map_users
                where state='{selected_state2}'
                group by year;"""
    df_result = pd.read_sql(query2, connection)
    fig = px.bar(df_result, x='year', y=['registered_users', 'app_opens'],barmode="stack",
                 title=f"Registered Users and App Opens in {selected_state2} Over Years")
    st.plotly_chart(fig)

    st.subheader("Device brand VS Registered/UnRegistered users")
    col1, col2 = st.columns(2)
    statename_query3 = "select distinct State from aggregated_users"
    year_query3 = "select distinct year from aggregated_users"
    states3 = pd.read_sql(statename_query3, connection)
    years3 = pd.read_sql(year_query3, connection)
    with col1:
        selected_state3 = st.selectbox("State", states3['State'])
    with col2:
        selected_year3 = st.selectbox("Year", years3['year'])
    query3 = f"""SELECT a.state,a.year,SUM(m.registered_user) AS total_registered_users,
                    a.user_brand AS device_brand,SUM(a.user_count) AS registered_users
                    FROM aggregated_users a
                    JOIN map_users m
                    ON a.state = m.state AND a.year = m.year
                    Where a.state = '{selected_state3}' AND a.year = '{selected_year3}'
                    GROUP BY a.state, a.year, a.user_brand;"""
    df_result = pd.read_sql(query3, connection)
    # Create unregistered users column
    df_result["Unregistered_Users"] = df_result["total_registered_users"] - df_result["registered_users"]
    # Melt for plotting
    df_melt = df_result.melt(
                                id_vars=["state", "year", "device_brand"],
                                value_vars=["registered_users", "Unregistered_Users"],
                                var_name="User Type",
                                value_name="Count"
                        )
    fig = px.bar(
                    df_melt,
                    x="device_brand",
                    y="Count",
                    color="User Type",
                    facet_col="state",
                    barmode="group",
                    title="Registered vs Unregistered Users by Device Brand & State"
                )
    st.plotly_chart(fig)

    st.subheader("Top device brands used by registered user on each state")
    query4 = """SELECT state, user_brand as device_brand, user_count as registered_users
                FROM (
                    SELECT 
                        state,
                        user_brand,
                        user_count,
                        RANK() OVER (PARTITION BY state ORDER BY user_count DESC) AS rnk
                    FROM aggregated_users
                ) t
                WHERE rnk = 1;"""
    df_result = pd.read_sql(query4, connection)
    # Group by Device Brand
    df_grouped = df_result.groupby("device_brand", as_index=False)["registered_users"].sum()
    fig = px.pie(
                df_grouped,
                names="device_brand",
                values="registered_users",
                hole=0.4
            )
    st.plotly_chart(fig)

    st.subheader("Top 3 / Bottom 3 District contribution to App opens")
    col1, col2 = st.columns(2)
    statename_query5 = "select distinct State from aggregated_users"
    year_query5 = "select distinct year from aggregated_users"
    states5 = pd.read_sql(statename_query5, connection)
    years5 = pd.read_sql(year_query5, connection)
    with col1:
        selected_state5 = st.selectbox("ChooseState", states5['State'])
    with col2:
        selected_year5 = st.selectbox("Choose Year", years5['year'])
    query5 = f"""SELECT state,district,SUM(app_opens) AS total_app_opens,
                RANK() OVER (
                    PARTITION BY state, year 
                    ORDER BY SUM(app_opens) ASC
                ) AS rnk
                FROM map_users 
                where state = '{selected_state5}' and year='{selected_year5}'and app_opens!=0 
                GROUP BY state, year,district"""                            
    df_result = pd.read_sql(query5, connection)
    # Sort data
    df_sorted = df_result.sort_values(by="rnk", ascending=False)
    # Top 3 and Bottom 3
    top3 = df_sorted.head(3)
    bottom3 = df_sorted.tail(3)
    df_combined = pd.concat([top3, bottom3])
    fig = px.bar(data_frame=df_combined,x="district",y="total_app_opens",color="district")
    st.plotly_chart(fig)
    