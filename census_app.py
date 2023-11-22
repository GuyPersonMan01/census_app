import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
    # Load the Adult Income dataset into DataFrame.
    df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)

    # Rename the column names in the DataFrame.
    column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    for i in range(df.shape[1]):
        df.rename(columns={i:column_name[i]},inplace=True)

    # Replace the invalid values ' ?' with 'np.nan'.
    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)

    # Delete the rows with invalid values and the column not required
    df.dropna(inplace=True)
    df.drop(columns='fnlwgt',axis=1,inplace=True)

    return df

census_df = load_data()

# Add a checkbox widget
show_census_data = st.checkbox("Show Census Data")

# Check if the checkbox is clicked
if show_census_data:
    # Display the subheader
    st.subheader("Census Data set")

    # Display the original Adult Income dataset
    st.write(census_df)

    # Display the number of rows and columns of the dataset
    num_rows = census_df.shape[0]
    num_cols = census_df.shape[1]
    st.write(f"Number of rows: {num_rows}")
    st.write(f"Number of columns: {num_cols}")

