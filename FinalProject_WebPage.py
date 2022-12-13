#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
#df = outcomedf.copy()
df=pd.read_csv('Metadata.csv')
st.title('Flight Ticket Price Prediction')
st.write('Hello, *World!* :sunglasses: Welcome to Our Final Project WebPage....')
st.write('The page shows expected flight ticket prices in the next 60 days')
st.write('Happy Landings!! - Vishnu & Christy')
st.subheader('Data Trend')
st.dataframe(df)
st.subheader('Data Numerical Statistic')
st.dataframe(df.describe())
st.subheader('Data Visualizations')
left_column, right_column = st.columns(2)
with left_column:
   #'Numerical Plot'
    num_feat = st.selectbox(
   'Select Numerical Feature', df.select_dtypes('number').columns)
    fig = px.scatter(df, x="Date", y=num_feat, title='Flight Cost Trend',color="Date")
st.plotly_chart(fig, use_container_width=True)
with right_column:
   #'Categorical column'
    fig =px.bar(df, x="Date", y=num_feat, title='Flight Cost Trend',color="Date")
st.plotly_chart(fig, use_container_width=True)
