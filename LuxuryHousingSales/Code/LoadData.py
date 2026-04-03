import pandas as pd
import mysql.connector
import DataCleaning as dc

database_connection = mysql.connector.connect(
    user="root",
    host="localhost",
    password="Nisha@2506",
    database="luxury_housing_sales"
)
my_cursor = database_connection.cursor()
# my_cursor.execute("create database luxury_housing_sales")

def sql_statements():
    my_cursor.execute("""create table if not exists luxury_housing_bglr(
                        Property_ID           varchar(25),        
                        Micro_Market          varchar(25),
                        Project_Name          varchar(25),
                        Developer_Name        varchar(25),
                        Unit_Size_Sqft        float,
                        Configuration         varchar(25),
                        Ticket_Price_Cr       float,      
                        Transaction_Type      varchar(25),        
                        Buyer_Type            varchar(25),        
                        Purchase_Quarter      date,
                        Connectivity_Score    float,       
                        Amenity_Score         float,       
                        Possession_Status     varchar(25),        
                        Sales_Channel         varchar(25),        
                        NRI_Buyer             varchar(10),        
                        Locality_Infra_Score  float,       
                        Avg_Traffic_Time_Min  int,         
                        Buyer_Comments        varchar(255),   
                        Developer_Name_encoded  int,
                        Micro_Market_encoded    int,     
                        Price_per_Sqft        float,        
                        Quarter_Number        int,          
                        Booking_Flag          int
                      )""")
    # insert into database
    df_data = dc.data_preprocessing().values.tolist()
    query ="insert into luxury_housing_bglr values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    for i in df_data:
        my_cursor.execute(query, tuple(i))
    database_connection.commit()

sql_statements()
my_cursor.close()
database_connection.close()