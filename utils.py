import pandas as pd

def load_data():
    """Load the titanic dataset and return it as a DataFrame."""
    df = pd.read_csv('data/titanic.csv')
    return df
