# -*- coding: utf-8 -*-
"""Data Profiling Tool.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gMFnPZonnOanaIXD4FQE4hx8JGNtflJb
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path):
    """Load the dataset from a given file path"""
    return pd.read_csv(file_path)


def data_summary(df):
    """Return a summary of the dataset"""
    return df.describe(include='all')


def data_types_detection(df):
    """Detect and return data types of each column in the dataset"""
    return df.dtypes


def unique_values(df):
    """Return unique values for each column in the dataset"""
    return df.nunique()


def top_frequent_values(df, N):
    """Return top N frequent values for each column in the dataset"""
    top_values = {}
    for column in df.columns:
        top_values[column] = df[column].value_counts().head(N).to_dict()
    return top_values


def plot_numeric(df, column):
    """Plot histogram for numeric columns"""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=30, kde=True)
    plt.title(f"Histogram of {column}")
    plt.show()


def plot_categorical(df, column):
    """Plot bar chart for categorical columns"""
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=column)
    plt.title(f"Bar Chart of {column}")
    plt.xticks(rotation=45)
    plt.show()


# Running the main part of the code
if __name__ == "__main__":
    # Load the data
    file_path = '/content/drive/MyDrive/Android Session 14-10-22/Python_project/demo_data.csv'  # Make sure this file is in the same directory as your script
    df = load_data(file_path)

    # Display Data Summary
    print(data_summary(df))

    # Display Data Types
    print(data_types_detection(df))

    # Display Unique Values
    print(unique_values(df))

    # Display Top Frequent Values
    N = 5  # Displaying top 5 values for simplicity
    print(top_frequent_values(df, N))

    # Visualization
    columns = df.columns.tolist()
    for column in columns:
        if df[column].dtype in ["int64", "float64"]:
            plot_numeric(df, column)
        else:
            plot_categorical(df, column)

