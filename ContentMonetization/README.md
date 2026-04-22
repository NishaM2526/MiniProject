# YouTube Content Monetization Analysis

This project analyzes YouTube video data to predict ad revenue potential and determine monetization eligibility using machine learning techniques.

## Project Overview

The application uses a Linear Regression model trained on YouTube video metrics to predict advertisement revenue in USD. It includes data preprocessing, model training, and a Streamlit web interface for user-friendly predictions.

## Features

- **Data Preprocessing**: Cleans and prepares YouTube video data including handling missing values, encoding categorical variables, and feature engineering
- **Machine Learning Model**: Linear Regression model for revenue prediction
- **Web Application**: Streamlit-based interface for real-time monetization analysis
- **Interactive Predictions**: Input video metrics to get revenue estimates and monetization potential

## Dataset

The project uses a YouTube ad revenue dataset containing video metrics such as:
- Views, likes, comments
- Watch time and video length
- Subscriber count
- Video category
- Country and device information

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ContentMonetization
```

2. Create and activate a virtual environment:
```bash
python -m venv env
env\Scripts\activate  # On Windows
```

3. Install required packages:
```bash
pip install pandas scikit-learn joblib streamlit
```

## Usage

### Training the Model

Run the model training script:
```bash
python Code/LinearRegressionModel.py
```

### Running the Web Application

Start the Streamlit app:
```bash
streamlit run App/YoutubeMonetization.py
```

Open your browser to `http://localhost:8501` and input your video metrics to get predictions.

### Data Preprocessing

To preprocess the data:
```python
from Code.Preprocess import data_preprocessing
df = data_preprocessing()
```

## Project Structure

```
ContentMonetization/
├── App/
│   ├── YoutubeMonetization.py        # Streamlit web app
│   └── RevenuePrediction.py          # Revenue prediction logic
├── Code/
│   ├── LinearRegressionModel.py      # Model training script
│   ├── Preprocess.py                 # Data preprocessing functions
│   ├── DataAnalysisNotebook.ipynb    # Data analysis notebook
│   ├── ModelBuildingNotebook.ipynb   # Model building notebook
│   └── PreprocessingNotebook.ipynb   # Preprocessing notebook
├── Data/
│   ├── youtube_ad_revenue_dataset.csv           # Raw dataset
│   └── Preprocessed_youtube_ad_revenue_dataset.csv  # Processed data
├── env/
│   └── ...                           # Virtual environment files
└── README.md                         # This file
```

## Model Details

- **Algorithm**: Linear Regression
- **Target Variable**: Ad revenue in USD
- **Features**: Views, likes, comments, watch time, video length, subscribers, category, engagement rate
- **Evaluation**: Mean Squared Error, R² Score

## Requirements

- Python 3.7+
- pandas
- scikit-learn
- joblib
- streamlit

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.