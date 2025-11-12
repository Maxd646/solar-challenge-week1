import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

def plot_boxplot(df, metric):
    fig, ax = plt.subplots()
    sns.boxplot(x='Country', y=metric, data=df, ax=ax)
    st.pyplot(fig)
