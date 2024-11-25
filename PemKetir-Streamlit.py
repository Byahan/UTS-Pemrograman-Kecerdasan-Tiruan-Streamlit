import pandas as pd
import streamlit as st

# Load the dataset
file_path = "C:/Users/Erlan/Desktop/ray/drug200.csv" #Use your local dataset path
data = pd.read_csv(file_path)

# Select numeric columns
numeric_data = data[["Age", "Na_to_K"]]

# Display the cleaned data in Streamlit app
st.write("Dataset Overview:")
st.write(data.head())

# Plot the line chart
st.line_chart(numeric_data)

# Optional: Describe the numeric columns
st.write("Dataset Description:")
st.write(numeric_data.describe())
