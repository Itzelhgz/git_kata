import pandas as pd

def load_data():
    """Load titanic dataset and return only male passengers."""
    df = pd.read_csv('data/titanic.csv')
    df = df[df['sex'] == 'male']
    return df

def clean_data(df):
    """
    Clean the input DataFrame.

    Parameters:
        df (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    # Drop rows where important columns are missing
    df = df.dropna(subset=['pclass', 'sex', 'age'])

    # Convert categorical columns to lowercase
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower()

    return df