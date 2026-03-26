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

def get_case_study_content():
        st.subheader("State-wise Transaction Analysis")
        statename_query = "select distinct State from aggregated_transaction"
        states = pd.read_sql(statename_query, connection)
        selected_state = st.selectbox("Select a State", states['State'])
        query1 = f"""select year,sum(transaction_count) as total_transaction_count,sum(transaction_amount) as total_transaction_amount
		            from phone_pe_pulse.aggregated_transaction
    		        where state='{selected_state}'
    		        group by year"""
        df_result = pd.read_sql(query1, connection)
        fig1 = px.line(df_result, x='year', y='total_transaction_count', 
                       title=f'Transaction Count Over Years in {selected_state}')
        fig2 = px.line(df_result, x='year', y='total_transaction_amount', 
                       title=f'Transaction Amount Over Years in {selected_state}')
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1)
        with col2:
            st.plotly_chart(fig2)

        st.subheader("Overall Payment categories")
        query2 ="""select Transaction_type,sum(transaction_count) as total_transaction_count,
                    sum(Transaction_amount) as total_transaction_amount     
                    from phone_pe_pulse.aggregated_transaction
                    group by Transaction_type"""
        df_result = pd.read_sql(query2, connection)
        fig1 = px.pie(df_result, names='Transaction_type', values='total_transaction_count', 
                      title='Transaction Count by Payment Category')
        fig2 = px.pie(df_result, names='Transaction_type', values='total_transaction_amount', 
                      title='Transaction Amount by Payment Category')   
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1)
        with col2:
            st.plotly_chart(fig2)

        st.subheader("Average transaction count for each Payment category")
        col1, col2 = st.columns(2)
        statename_query3 = "select distinct State from aggregated_transaction"
        year_query3 = "select distinct year from aggregated_transaction"
        states3 = pd.read_sql(statename_query3, connection)
        years3 = pd.read_sql(year_query3, connection)
        with col1:
            selected_state3 = st.selectbox("Select State", states3['State'])
        with col2:
            selected_year3 = st.selectbox("Select Year", years3['year'])
        query3 = f"""select Transaction_type,avg(Transaction_count) as avg_transaction_count
                        from phone_pe_pulse.aggregated_transaction
                        where year= '{selected_year3}' and state='{selected_state3}'
                        group by year,Transaction_type"""
        df_result = pd.read_sql(query3, connection)
        fig = px.bar(df_result, x='Transaction_type', y='avg_transaction_count', 
                     title=f'Average Transaction Count by Payment Category in {selected_state3} for {selected_year3}')
        st.plotly_chart(fig)

        st.subheader("Top/Bottom 10 states with high transaction count")
        query4a="""select state, sum(transaction_count) as transaction_count
		            from phone_pe_pulse.aggregated_transaction
                    group by state order by transaction_count desc limit 10 """
        df_result1 = pd.read_sql(query4a, connection)
        query4b="""select state, sum(transaction_count) as transaction_count
		            from phone_pe_pulse.aggregated_transaction
                    group by state order by transaction_count asc limit 10"""
        df_result2 = pd.read_sql(query4b, connection)
        fig1 = px.bar(df_result1, x='transaction_count', y='state', orientation='h',
                      title='Top 10 States by Transaction Count')
        fig2 = px.bar(df_result2, x='transaction_count', y='state', orientation='h',
                      title='Bottom 10 States by Transaction Count')
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1)
        with col2:
            st.plotly_chart(fig2)

        st.subheader("Average transaction received on Quarterly basis")
        col1, col2 = st.columns(2)
        statename_query5 = "select distinct State from aggregated_transaction"
        year_query5 = "select distinct year from aggregated_transaction"
        states5 = pd.read_sql(statename_query5, connection)
        years5 = pd.read_sql(year_query5, connection)
        with col1:
            selected_state5 = st.selectbox("State", states5['State'])
        with col2:
            selected_year5 = st.selectbox("Year", years5['year'])
        query5=f""" select quarter,avg(transaction_count)
                    from phone_pe_pulse.aggregated_transaction
                    where year='{selected_year5}' and state='{selected_state5}'
                    group by state,year,quarter"""   
        df_result = pd.read_sql(query5, connection)   
        fig = px.line(df_result, x='quarter', y='avg(transaction_count)',
                      title=f'Average Transaction Count by Quarter in {selected_state5} for {selected_year5}')
        st.plotly_chart(fig)
