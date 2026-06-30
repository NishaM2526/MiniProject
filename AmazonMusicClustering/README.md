# Amazon Music Clustering

A machine learning project that clusters songs based on audio features using K-Means clustering algorithm.

## 📊 Project Overview

This project analyzes Amazon Music dataset and groups songs into distinct clusters based on their audio characteristics like danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, and tempo.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn (K-Means)
- **Visualization:** Matplotlib, Seaborn
- **Web App:** Streamlit

## 📁 Project Structure

```
AmazonMusicClustering/
├── App/
│   ├── MusicRecommandation.py    # Streamlit web application
│   └── config.toml               # Configuration file
├── Code/
│   ├── DataAnalysisNotebook.ipynb # Data exploration
│   ├── MLAlgorithm.ipynb          # ML model building
│   └── PreProcessingNotebook.ipynb # Data preprocessing
├── Data/
│   ├── clustered_songs.csv       # Final clustered dataset
│   ├── single_genre_artists_cleaned.csv
│   └── single_genre_artists.csv
├── image/
│   └── scaled/                   # Scaled images
└── env/
    └── MusicRecommandation.py    # Virtual environment script
```

## 🎵 Features Used for Clustering

| Feature | Description |
|---------|-------------|
| Danceability | Describes how suitable a track is for dancing |
| Energy | Represents a perceptual measure of intensity and activity |
| Loudness | Overall loudness of the track in decibels |
| Speechiness | The presence of spoken words in the track |
| Acousticness | A confidence measure of whether the track is acoustic |
| Instrumentalness | Predicts whether a track contains no vocals |
| Liveness | Detects the presence of an audience in the recording |
| Valence | Describes the musical positiveness conveyed by a track |
| Tempo | The overall estimated tempo of a track in BPM |

## 🔬 Methodology

1. **Data Preprocessing**
   - Data cleaning and handling missing values
   - Feature selection based on audio characteristics

2. **Feature Scaling**
   - Applied StandardScaler to normalize features
   - Ensures all features contribute equally to clustering

3. **Model Building**
   - Used K-Means clustering algorithm
   - Evaluated using Silhouette Score and Inertia
   - Tested clusters from k=2 to k=10

4. **Cluster Analysis**
   - Identified distinct song categories
   - Assigned meaningful cluster names

## 📈 Results

The final model uses **3-4 clusters** based on:
- Low inertia values
- High silhouette scores

### Cluster Categories:
- **Cluster 0:** Party / Energetic
- **Cluster 1:** [To be defined based on analysis]
- **Cluster 2:** Chill / Soft
- **Cluster 3:** [To be defined based on analysis]
- **Cluster 4:** [To be defined based on analysis]

## 🚀 How to Run

1. **Activate Virtual Environment**
   ```bash
   cd AmazonMusicClustering
   env\Scripts\activate
   ```

2. **Run Streamlit App**
   ```bash
   streamlit run App/MusicRecommandation.py
   ```

3. **Open in Browser**
   Navigate to `http://localhost:8501`

## 📱 Application Features

- Interactive song clustering visualization
- Dataset preview with cluster information
- Sample songs from each cluster
- Audio feature analysis

## 📄 Documentation

- [Summary Report](AmazonMusicClustering-SummaryReport.docx)

## 👤 Author

Nisha M

## 📅 Date

April 2026