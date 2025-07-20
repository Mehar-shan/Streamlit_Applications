import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# add title
st.title('Data Analysis Application')
st.subheader('This is a simple data analysis application created by @codanics')

# create a dropdown list to choose a dataset
dataset_options = ['iris', 'titanic', 'tips', 'diamonds']
selected_dataset = st.selectbox('Select a dataset', dataset_options)

# load the selected dataset
if selected_dataset == 'iris':
    df = sns.load_dataset('iris')
elif selected_dataset == 'titanic':
    df = sns.load_dataset('titanic')
elif selected_dataset == 'tips':
    df = sns.load_dataset('tips')
elif selected_dataset == 'diamonds':
    df = sns.load_dataset('diamonds')

# button to upload custom dataset
uploaded_file = st.file_uploader('Upload a custom dataset', type=['csv', 'xlsx'])

if uploaded_file is not None:
    # process the uploaded file
    df = pd.read_csv(uploaded_file)  # assuming the uploaded file is in CSV format

# display the dataset
st.write(df)

# display the number of Rows and Column from the selected data
st.write('Number of Rows:', df.shape[0])
st.write('Number of Columns:', df.shape[1])

# display the column names of selected data with their data types
st.write('Column Names and Data Types:', df.dtypes)
# print the null vales of selected data
if df.isnull().sum().sum() > 0 :
    st.write('Null Values:', df.isnull().sum())
else:
    st.write('No Null Values Found')    
# display the summary of selected data
st.write(df.describe())
# create a pairplot of selected data
st.subheader('Pairplot')
# select the columns to be used as hue in pairplot
selected_hue = st.selectbox('Select a column to use as hue', df.columns)
st.pyplot(sns.pairplot(df))
# select the coumns which are numeric and make a heatmap
# Create a heatmap
st.subheader('Heatmap')
# select the columns which are numeric and then create a corr_matrix
numeric_columns = df.select_dtypes(include=np.number).columns
corr_matrix = df[numeric_columns].corr()
numeric_columns = df.select_dtypes(include=np.number).columns
corr_matrix = df[numeric_columns].corr()

from plotly import graph_objects as go

# Convert the seaborn heatmap plot to a Plotly figure
heatmap_fig = go.Figure(data=go.Heatmap(z=corr_matrix.values,
                                       x=corr_matrix.columns,
                                       y=corr_matrix.columns,
                                       colorscale='Viridis'))
st.plotly_chart(heatmap_fig)
