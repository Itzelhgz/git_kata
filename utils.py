import pandas as pd

def load_data():
    """Load titanic dataset and return only male passengers."""
    df = pd.read_csv('data/titanic.csv')
    df = df[df['Sex'] == 'male']
    return df