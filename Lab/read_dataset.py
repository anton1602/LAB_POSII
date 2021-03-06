import pandas as pd


def get_breast_cancer_dataset():
    df = pd.read_csv(r'heart.csv')
    return df.drop('target', axis=1), df['target']
