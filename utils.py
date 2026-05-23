import pandas as pd

def load_data():
    """Load titanic dataset and return only male passengers."""
    df = pd.read_csv('data/titanic.csv')
    df = df[df['Sex'] == 'male']
    return df

def clean_data(df):
    """
    Cleans the Titanic dataset.

    Parameters:
        df (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Cleaned dataframe
    """

    # Drop rows with missing values
    df = df.dropna()

    # Convert categorical columns to lowercase
    categorical_columns = df.select_dtypes(include=["object"]).columns

    for col in categorical_columns:
        df[col] = df[col].str.lower()

    return df