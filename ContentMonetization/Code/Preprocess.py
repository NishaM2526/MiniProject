import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

base_dir = os.path.dirname(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
file_path = os.path.join(base_dir, "Data", "youtube_ad_revenue_dataset.csv")
df = pd.read_csv(file_path)

def data_preprocessing():
    # Creating a copy of the original DataFrame to work with
    df_copy = df.copy()

    # Handle missing values
    df_copy=df_copy.dropna(subset=['likes','comments','watch_time_minutes'], how='all') 
    df_copy=df_copy.dropna(subset=['likes','comments'], how='all') 
    df_copy=df_copy.fillna({'watch_time_minutes':df_copy['watch_time_minutes'].median()})
    df_copy['likes'] = df_copy['likes'].fillna(0)
    df_copy['likes'] = df_copy['likes'].astype(int)
    df_copy['comments'] = df_copy['comments'].fillna(0)
    df_copy['comments'] = df_copy['comments'].astype(int)

    # delete the duplicate rows and keep the first occurrence
    df_copy=df_copy.drop_duplicates(keep='first')

    # Label encoding
    encoder =LabelEncoder()
    df_copy['category']=pd.to_numeric(encoder.fit_transform(df_copy['category']),errors='coerce')

    df_copy=df_copy.drop(columns=['video_id']) 
    df_copy=df_copy.drop(columns=['date']) 
    df_copy=df_copy.drop(columns=['country']) 
    df_copy=df_copy.drop(columns=['device'])
        
    # Feature engineering
    df_copy['engagement_rate'] = (df_copy['likes'] + df_copy['comments']) / df_copy['views']

    return df_copy

#print(data_preprocessing().head())