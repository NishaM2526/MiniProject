import os
import streamlit as st
import torch
import pickle
import tensorflow as tf
import re
import emoji
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from torch import nn
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

base_dir = os.path.dirname(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
model_path = os.path.join(base_dir, "Model", "best_bilstm_model.pth")
vector_path = os.path.join(base_dir, "Model", "vocab.pkl")
train_data_path = os.path.join(base_dir, "Data", "train.csv")

st.set_page_config(page_title="Toxic Comment Detection",layout="wide")
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

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.25rem;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

# Initialize preprocessing components
lemmatizer = WordNetLemmatizer()
sw = stopwords.words('english')

# Preprocessing the comments
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|https\S+|www\S+','',text)
    text = re.sub(r"<.*?>",'',text)
    text = re.sub(r'@\w+|#\w+','',text)
    text = re.sub(r'(.)\1{2,}',r'\1\1',text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = emoji.replace_emoji(text, '')
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in sw]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)

# BiLSTM Model Class
class BiLSTM(nn.Module):
    def __init__(self,vocab_size,embed_size,hidden_size,output_size):
        super(BiLSTM,self).__init__()
        self.embedding = nn.Embedding(vocab_size,embedding_dim=embed_size,padding_idx=0)
        # Bidirectional LSTM
        self.lstm = nn.LSTM(embed_size,hidden_size,num_layers=1,batch_first=True,bidirectional=True)
        self.dropout = nn.Dropout(0.5)
        self.fc = nn.Linear(hidden_size * 2,output_size)
        
    def forward(self,X):
        X = self.embedding(X)
        out,(ht, ct) =self.lstm(X)
        forward_hidden = ht[-2]
        backward_hidden = ht[-1]
        out = torch.cat((forward_hidden, backward_hidden), dim=1)
        out = self.dropout(out)
        out = self.fc(out)
        return out

# Load the trained model
@st.cache_resource
def load_model():
    checkpoint = torch.load(model_path,map_location=torch.device('cpu')
    )
    model = BiLSTM(
        checkpoint['vocab_size'],
        checkpoint['embed_size'],
        checkpoint['hidden_size'],
        checkpoint['output_size']
    )
    model.load_state_dict(
        checkpoint['model_state_dict']
    )
    model.eval()
    return model

model = load_model()

# Load vectorizer
@st.cache_resource
def load_vectorizer():

    with open(vector_path,"rb") as f:
        vocab = pickle.load(f)

    vectorizer = tf.keras.layers.TextVectorization(
        max_tokens=30000,
        output_sequence_length=100,
        output_mode='int',
        vocabulary=vocab
    )
    return vectorizer
vectorizer = load_vectorizer()

# Model prediction function
def predict_toxicity(text):
    cleaned = clean_text(text)
    vector = vectorizer([cleaned]).numpy()
    vector = torch.tensor(vector,dtype=torch.long)
    with torch.no_grad():
        output = model(vector)
        probability = torch.sigmoid(output).item()
    threshold = 0.6
    label = (
        "Toxic"
        if probability > threshold
        else "Non-Toxic"
    )
    return label, probability

st.title("Toxic Comment Detection System", text_alignment="center")

tab1, tab2, tab3 = st.tabs(
    [
        "**Single Prediction**",
        "**Bulk Prediction**",
        "**Model Dashboard**"
    ]
)

with tab1:
    st.header("Comment Prediction")
    comment = st.text_area("Enter Comment")
    if st.button("Predict"):
        label, prob = predict_toxicity(comment)
        st.subheader(f"Prediction: {label}")
        st.metric("Toxicity Probability",f"{prob:.2%}")

with tab2:
    uploaded_file = st.file_uploader("Upload CSV",type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        predictions = []
        probabilities = []
        for text in df['comment_text']:
            label, prob = predict_toxicity(text)
            predictions.append(label)
            probabilities.append(prob)
        df['Prediction'] = predictions
        df['Probability'] = probabilities
        st.dataframe(df)
        csv = df.to_csv(index=False)
        st.download_button("Download Results",csv,"toxicity_predictions.csv","text/csv")
    else:
        st.info("Please upload a CSV file containing a 'comment_text' column.")

with tab3:
    st.subheader("Bi-directional LSTM Model Performance")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Accuracy", "93.85%")
    col2.metric("Precision", "64.63%")
    col3.metric("Recall", "87.21%")
    col4.metric("F1 Score", "74.24%")

    st.subheader("Model Comparison - LSTM vs BiLSTM")
    col1, col2 = st.columns(2)
    with col1: 
        comparison = pd.DataFrame({
                                    "Metric":["Accuracy","Precision","Recall","F1 Score"],
                                    "LSTM":[93.97,66.00,83.94,73.89],
                                    "BiLSTM":[93.85,64.63,87.21,74.24]
                                })
        st.dataframe(comparison)
    
    st.subheader("Performance Visualization")
    fig = px.bar(
        comparison,
        x="Metric",
        y=["LSTM","BiLSTM"],
        barmode="group",
        title="LSTM vs BiLSTM Performance"
    )
    st.plotly_chart(fig)

    st.subheader("Confusion Matrix")
    col1, col2 = st.columns(2)
    with col1: 
        cm = np.array([
                        [27121,1549],
                        [415,2830]
                    ])
        fig, ax = plt.subplots()
        sns.heatmap(
            cm,
            annot=True,
            fmt='d',
            cmap='Blues',
            ax=ax
        )
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        ax.set_title("BiLSTM Confusion Matrix")
        st.pyplot(fig)

    st.subheader("Dataset Insights")
    df_train = pd.read_csv(train_data_path)
    df_train['toxicity_ind'] = df_train[['toxic',
                         'severe_toxic',
                         'obscene',
                         'threat',
                         'insult',
                         'identity_hate']].sum(axis=1)
    df_train['toxicity_ind'] = df_train['toxicity_ind'].apply(lambda x: 1 if x > 0 else 0)
    col1, col2 = st.columns(2)
    with col1: 
        st.write(f"Total Records: {len(df_train)}")
        toxicity_counts = df_train['toxicity_ind'].value_counts()
        fig = px.pie(
            values=toxicity_counts.values,
            names=["Non Toxic","Toxic"]
        )
        st.plotly_chart(fig)

    st.subheader("Sample TestCases")
    col1, col2 = st.columns(2)
    with col1:
        sample_df = pd.DataFrame({
                                    "Comment":[
                                        "Have a nice day",
                                        "Excellent work",
                                        "You are stupid",
                                        "I hate you"
                                    ],
                                    "Prediction":[
                                        "Non-Toxic",
                                        "Non-Toxic",
                                        "Toxic",
                                        "Toxic"
                                    ]
                                })
        st.table(sample_df)