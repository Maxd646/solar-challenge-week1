import streamlit as st
import pandas as pd
import sys
import os

# Add 'app' folder to Python path
sys.path.append(os.path.dirname(__file__))

from utils import load_data, plot_boxplot

st.title("Solar Data Dashboard")

# Select countries
countries = st.multiselect(
    "Select countries", ["Benin", "Sierra Leone", "Togo"], 
    default=["Benin", "Sierra Leone", "Togo"]
)

# Load datasets
dfs = []
if "Benin" in countries:
    df = load_data("data/benin_clean.csv")
    df['Country'] = "Benin"
    dfs.append(df)
if "Sierra Leone" in countries:
    df = load_data("data/sierra_leone_clean.csv")
    df['Country'] = "Sierra Leone"
    dfs.append(df)
if "Togo" in countries:
    df = load_data("data/togo_clean.csv")
    df['Country'] = "Togo"
    dfs.append(df)

if dfs:
    df_all = pd.concat(dfs)
    metric = st.selectbox("Select metric to plot", ["GHI","DNI","DHI"])
    plot_boxplot(df_all, metric)

    st.write("Top 5 highest GHI readings:")
    st.dataframe(df_all.sort_values("GHI", ascending=False).head())
