import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna(subset=['GHI','DNI','DHI'])
    df['ModA'] = df['ModA'].fillna(df['ModA'].mean())
    df['ModB'] = df['ModB'].fillna(df['ModB'].mean())
    return df

def save_cleaned(df, file_path):
    df.to_csv(file_path, index=False)
