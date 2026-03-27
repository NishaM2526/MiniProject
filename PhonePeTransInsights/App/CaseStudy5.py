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

def get_case_study_content5():
    st.subheader("Top States (Year + Quarter) - User registration data")
    col1, col2 = st.columns(2)
    year_query = "select distinct year from top_users_district"
    years = pd.read_sql(year_query, connection)
    quarter_query = "select distinct quarter from top_users_district"
    quarters = pd.read_sql(quarter_query, connection)
    with col1:
        selected_year = st.selectbox("Select a Year", years['year'])
    with col2:
        selected_quarter = st.selectbox("Select a Quarter", quarters['quarter'])
    query1 = f"""SELECT 
                    state,
                    SUM(registered_user) AS total_users
                FROM top_users_district
                WHERE year = {selected_year} AND quarter = {selected_quarter}
                GROUP BY state
                ORDER BY total_users DESC
                LIMIT 10;"""
    df_result = pd.read_sql(query1, connection)
    fig = px.bar(
                    df_result,
                    x="total_users",
                    y="state",
                    orientation="h",
                    text="total_users",
                    title=f"Top 10 States by Registered Users ({selected_year} Q{selected_quarter})"
                )
    fig.update_layout(
                    xaxis_title="Registered Users",
                    yaxis_title="State",
                    yaxis=dict(categoryorder='total ascending'),
                    template="plotly_white",
                    height=500
                    )
    st.plotly_chart(fig)

    st.subheader("Top Districts (Year + Quarter) - User registration data")
    col1, col2 = st.columns(2)
    year_query2 = "select distinct year from top_users_district"
    years2 = pd.read_sql(year_query2, connection)
    quarter_query2 = "select distinct quarter from top_users_district"
    quarters2 = pd.read_sql(quarter_query2, connection)
    with col1:
        selected_year = st.selectbox("Select Year", years2['year'])
    with col2:
        selected_quarter = st.selectbox("Select Quarter", quarters2['quarter'])
    query2 = f"""SELECT 
                    state,
                    district,
                    SUM(registered_user) AS total_users
                FROM top_users_district
                WHERE year = {selected_year} AND quarter = {selected_quarter}
                GROUP BY state, district
                ORDER BY total_users DESC
                LIMIT 5;"""
    df_result = pd.read_sql(query2, connection)
    # Pivot table
    heatmap_data = df_result.pivot(
        index='district',
        columns='state',
        values='total_users'
    ).fillna(0)
    fig = px.imshow(
                        heatmap_data,
                        text_auto=True,
                        aspect="auto",
                        title=f"District-wise User Registrations Heatmap ({selected_year} Q{selected_quarter})",
                        color_continuous_scale="YlGnBu"
                    )

    fig.update_layout(
                        xaxis_title="State",
                        yaxis_title="District",
                        height=600
                    )
    st.plotly_chart(fig)

    st.subheader("Top Pincodes (Year + Quarter) - User registration data")
    col1, col2 = st.columns(2)
    year_query3 = "select distinct year from top_users_pincode"
    years3 = pd.read_sql(year_query3, connection)
    quarter_query3 = "select distinct quarter from top_users_pincode"
    quarters3 = pd.read_sql(quarter_query3, connection)
    with col1:
        selected_year = st.selectbox("Year", years3['year'])
    with col2:
        selected_quarter = st.selectbox("Quarter", quarters3['quarter'])
    query3 = f"""SELECT 
                        state,
                        pincode,
                        SUM(registered_user) AS total_users
                    FROM top_users_pincode
                    WHERE year = {selected_year} AND quarter = {selected_quarter}
                    GROUP BY state, pincode
                    ORDER BY total_users DESC
                    LIMIT 5;"""
    df_result = pd.read_sql(query3, connection)
    fig = px.scatter(
                        df_result,
                        x="pincode",
                        y="total_users",
                        size="total_users",
                        color="state",
                        hover_name="pincode",
                        size_max=50,
                        title=f"Pincode-wise User Registration Analysis ({selected_year} Q{selected_quarter})"
                    )
    fig.update_layout(
                        xaxis_title="Pincode",
                        yaxis_title="Registered Users",
                        template="plotly_white",
                        height=600
                    )
    st.plotly_chart(fig)

    st.subheader("User growth momentum across states/districts")
    col1, col2 = st.columns(2)
    year_query4 = "select distinct year from top_users_district"
    years4 = pd.read_sql(year_query4, connection)
    statename_query4 = "select distinct State from top_users_district"
    states4 = pd.read_sql(statename_query4, connection)
    with col1:
        selected_year4 = st.selectbox("Choose Year", years4['year'])
    with col2:
        selected_state4 = st.selectbox("Select State", states4['State'])
    query4 = f"""SELECT 
                    state,
                    year,
                    SUM(CASE WHEN quarter = 4 THEN registered_user ELSE 0 END) as Q4_user,
                    SUM(CASE WHEN quarter = 1 THEN registered_user ELSE 0 END) as Q1_user,
                    SUM(CASE WHEN quarter = 4 THEN registered_user ELSE 0 END) -
                        SUM(CASE WHEN quarter = 1 THEN registered_user ELSE 0 END) AS total_growth
                    FROM top_users_district
                    where state='{selected_state4}' and year={selected_year4}
                    GROUP BY year,state;"""
    df_result = pd.read_sql(query4, connection)
    fig = go.Figure(go.Waterfall(
                                    x=["Q1_user", "total_growth", "Q4_user"],
                                    y=[df_result['Q1_user'].iloc[0], df_result['total_growth'].iloc[0], df_result['Q4_user'].iloc[0]],
                                    measure=["absolute", "relative", "total"],
                                    text=[df_result['Q1_user'].iloc[0], df_result['total_growth'].iloc[0], df_result['Q4_user'].iloc[0]],
                                    textposition="outside"
                                ))

    fig.update_layout(
                        title=f"{selected_state4} User Growth (Q1 → Q4)",
                        yaxis_title="Registered Users",
                        template="plotly_white"
                    )
    st.plotly_chart(fig)

    st.subheader("Top 5 User growth across states/pincodes")
    year_query5 = "select distinct year from top_users_pincode"
    years5 = pd.read_sql(year_query5, connection)
    selected_year5 = st.selectbox("Choose a Year", years5['year'])
    query5 = f"""SELECT 
                    state,
                    year,SUM(CASE WHEN quarter = 4 THEN registered_user ELSE 0 END) Q4_user,
                    SUM(CASE WHEN quarter = 1 THEN registered_user ELSE 0 END) Q1_user,
                    SUM(CASE WHEN quarter = 4 THEN registered_user ELSE 0 END) -
                        SUM(CASE WHEN quarter = 1 THEN registered_user ELSE 0 END) AS total_growth
                    FROM top_users_pincode
                    where year='{selected_year5}'
                    GROUP BY year,state
                    order by total_growth desc limit 5;"""
    df_result = pd.read_sql(query5, connection)
    df = df_result.sort_values(by="total_growth", ascending=True)

    fig = go.Figure()

    # Add connecting lines
    for i in range(len(df)):
        fig.add_trace(go.Scatter(
            x=[df["Q1_user"][i], df["Q4_user"][i]],
            y=[df["state"][i], df["state"][i]],
            mode="lines",
            line=dict(width=2, color="gray"),
            showlegend=False
        ))

        # Add Q1 points
        fig.add_trace(go.Scatter(
            x=df["Q1_user"],
            y=df["state"],
            mode="markers",
            name="Q1",
            marker=dict(size=10, color="blue")
        ))

        # Add Q4 points
        fig.add_trace(go.Scatter(
            x=df["Q4_user"],
            y=df["state"],
            mode="markers",
            name="Q4",
            marker=dict(size=10, color="green")
        ))

        fig.update_layout(
            title="State-wise Growth in Registered Users (Q1 vs Q4)",
            xaxis_title="Registered Users",
            yaxis_title="State",
            template="plotly_white",
            height=500
        )

    st.plotly_chart(fig)