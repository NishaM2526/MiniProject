import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

base_dir = os.path.dirname(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
file_path = os.path.join(base_dir, "Data", "Luxury_Housing_Bangalore.csv")
df = pd.read_csv(file_path)

def data_preprocessing():
    # Creating a copy of the original DataFrame to work with
    df_copy = df.copy()

    # Clean inconsistent formats
    df_copy['Ticket_Price_Cr']=df_copy['Ticket_Price_Cr'].str.replace('Cr','')
    df_copy['Ticket_Price_Cr']=df_copy['Ticket_Price_Cr'].str.replace('₹','')
    df_copy['Ticket_Price_Cr']=df_copy['Ticket_Price_Cr'].astype(float)

    # Normalize text fields
    encoder = LabelEncoder()
    df_copy['Configuration']=df_copy['Configuration'].str.upper()
    df_copy['Micro_Market'] = df_copy['Micro_Market'].str.strip().str.lower()
    df_copy['Micro_Market'] = df_copy['Micro_Market'].str.strip().str.title()
    df_copy['NRI_Buyer'] = df_copy['NRI_Buyer'].str.strip().str.title()
    df_copy['Developer_Name_encoded'] = encoder.fit_transform(df_copy['Developer_Name'])
    df_copy['Micro_Market_encoded'] = encoder.fit_transform(df_copy['Micro_Market'])

    # Handle missing values
    df_copy=df_copy.dropna(subset=['Unit_Size_Sqft','Ticket_Price_Cr','Amenity_Score'], how='all') 
    df_copy=df_copy.dropna(subset=['Unit_Size_Sqft','Ticket_Price_Cr'], how='all') 
    df_copy=df_copy.fillna(
                            {   
                                'Unit_Size_Sqft':df_copy['Unit_Size_Sqft'].mean(),
                                'Ticket_Price_Cr':df_copy['Ticket_Price_Cr'].median(),
                                'Amenity_Score':df_copy['Amenity_Score'].median()
                            }
                        )
    df_copy=df_copy.fillna({'Buyer_Comments': df_copy['Buyer_Comments'].ffill()})

    # Handle duplicates
    df_copy=df_copy.drop_duplicates(keep='first')

    # Derive columns
    df_copy['Price_per_Sqft'] = ((df_copy['Ticket_Price_Cr']*10000000)/df_copy['Unit_Size_Sqft']).round(2)
    df_copy['Purchase_Quarter']=pd.to_datetime(df_copy['Purchase_Quarter'])
    df_copy['Quarter_Number']=df_copy['Purchase_Quarter'].dt.quarter
    df_copy['Booking_Flag']=df_copy['Transaction_Type'].apply(lambda x: 1 if x=='Primary' else 0)

    return df_copy

#df_data_cleaned = data_preprocessing()
#print(df_data_cleaned.head())