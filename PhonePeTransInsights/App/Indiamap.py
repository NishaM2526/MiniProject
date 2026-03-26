import pandas as pd
import plotly.express as px
import mysql.connector

# SQL connection
connection = mysql.connector.connect(
    user="root",
    host="localhost",
    password="Nisha@2506",
    database="phone_pe_pulse"
)

cursor = connection.cursor()

def load_map():
    sql_query = """select State,transaction_count,transaction_amount
                    from all_transaction
                    where year='2024'"""
    cursor.execute(sql_query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['State', 'all_transaction','transaction_value'])
    
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='all_transaction',
        color_continuous_scale='bluyl',
        hover_data=["all_transaction", "transaction_value"],
        labels={'all_transaction': 'All Transactions', 'transaction_value': 'Total Payment Value'},
    )

    fig.update_geos(fitbounds="locations", visible=False,lonaxis={'range': [68, 98]},lataxis={'range': [6, 38]})
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=550,width=550)

    return fig
