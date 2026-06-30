import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

st.set_page_config(page_title="Music Clustering App", layout="wide")
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
st.title("Amazon Music Clustering", text_alignment="center")

def style_dataframe(df):
    return df.style.set_table_styles(
        [{
            'selector': 'th',
            'props': [
                ('background-color', 'darkGoldenrod'),
                ('color', 'white'),
                ('font-family', 'Arial, sans-serif'),
                ('font-size', '13px')
            ]
        }]
    )

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\nisha\OneDrive\Desktop\Nisha\GUVI\MiniProject\AmazonMusicClustering\Data\clustered_songs.csv")
    return df

df = load_data()

def dataset():
    st.write("Here's a preview of the cleaned dataset with cluster information:")
    dataset_df = df.groupby('cluster').apply(lambda x: x.sample(2)).reset_index(drop=True)
    dict_name = {'name_song': 'Song Name', 'danceability': 'Danceability', 'energy': 'Energy', 'loudness': 'Loudness',
            'speechiness': 'Speechiness', 'acousticness': 'Acousticness', 'instrumentalness': 'Instrumentalness',
            'liveness': 'Liveness', 'valence': 'Valence', 'tempo': 'Tempo', 'genres': 'Genres', 'cluster': 'Cluster',
            'cluster_name': 'Cluster Name'}
    dataset_df.rename(columns=dict_name,inplace=True)
    styled_df = style_dataframe(dataset_df)
    #st.dataframe(styled_df)  
    st.write(styled_df.to_html(), unsafe_allow_html=True)

def fhist():
    st.subheader("Feature Distribution", text_alignment="center")
    image = Image.open(r"C:\Users\nisha\OneDrive\Desktop\Nisha\GUVI\MiniProject\AmazonMusicClustering\image\featureDistribution.png")
    st.write(' ')
    st.write(' ')
    st.image(image)

def kde():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.write(' ')
        st.write(' ')
        features = ['danceability','energy','loudness','speechiness',
                'acousticness','instrumentalness','liveness',
                'valence','tempo']
        selected_feature = st.selectbox("Feature", features)
        imagefolder = fr"C:\Users\nisha\OneDrive\Desktop\Nisha\GUVI\MiniProject\AmazonMusicClustering\image\scaled\{selected_feature}.png"
        image = Image.open(imagefolder)
        st.image(image)
        st.write("KDE plots - To visualize feature distributions before and after scaling.")
    with col3:
        st.write(' ')

def pca(): 
    st.write("The PCA plot below illustrates the distribution of songs across the three clusters. " \
    "The distinct separation between clusters indicates that the K-Means algorithm successfully grouped " \
    "songs with similar audio features together, providing insights into the underlying structure of the dataset.")   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        image = Image.open(r"C:\Users\nisha\OneDrive\Desktop\Nisha\GUVI\MiniProject\AmazonMusicClustering\image\pca.png")
        st.write(' ')
        st.write(' ')
        st.image(image)
        st.subheader("Cluster Visualization", text_alignment="center")
    with col3:
        st.write(' ')
    
# Cluster Insights
def clusters():    
    col1, col2, col3 = st.columns(3)    
    with col1:
        st.write(' ')
    with col2:
        st.write(' ')
        st.write(' ')
        st.write("The table below shows the distribution of songs across the 3 clusters. " )
        summary = df['cluster_name'].value_counts().reset_index()
        summary.columns = ['Cluster Name', 'Song Count']
        styled_df = style_dataframe(summary)
        st.write(styled_df.to_html(), unsafe_allow_html=True)
    with col3:
        st.write(' ')

def genres():
    col1, col2, col3 = st.columns(3)    
    with col1:
        st.write(' ')
    with col2:
        st.subheader("Top Genres in each Cluster", text_alignment="center")
        st.write(' ')
        top_genres_df = (
        df.groupby('cluster_name')['genres']
                    .value_counts()
                    .groupby(level=0)
                    .head(5)
                    .reset_index(name='count')
                    )
        top_genres_df.columns = ['Cluster Name', 'Genres', 'Total songs']
        styled_df = style_dataframe(top_genres_df)
        st.write(styled_df.to_html(), unsafe_allow_html=True)
    with col3:
        st.write(' ')

def songs():
    
    col1, col2 = st.columns(2)    
    with col1:
        selected_cluster = st.selectbox("Select Cluster",sorted(df['cluster_name'].unique()))
        songs = df[df['cluster_name'] == selected_cluster]['name_song'].dropna().unique()
        songs_df = pd.DataFrame(songs, columns=['Song Name'])
    with col2:    
        st.subheader(f"Songs in '{selected_cluster}' Cluster ({len(songs_df)})")    
        styled_df = style_dataframe(songs_df)
        st.dataframe(styled_df, use_container_width=True)  
        
pg = st.navigation( {
                    "": [st.Page(dataset,title="Dataset")],
                    "Analysis": [ st.Page(fhist,title="FeatureDistribution"),st.Page(kde,title="KDE Plots"), st.Page(pca,title="PCA")],
                    "Cluster Insights": [
                                            st.Page(clusters, title="Clusters Distribution"),
                                            st.Page(genres, title="Top Genres"),
                                            st.Page(songs, title="Top Songs")]
                    },
                    position="top"
                ) 
pg.run()
