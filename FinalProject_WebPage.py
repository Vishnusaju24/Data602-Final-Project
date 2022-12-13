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
st.write('The page shows predicted flight ticket prices on a given day based on state of the art model devolpment done on 60 days of data from the day')
st.write('Happy Landings!! - Vishnu & Christy')
st.subheader('Dataset')
st.dataframe(df)
st.subheader('Data Numerical Statistic')
st.dataframe(df.describe())
st.subheader('Data Visualization with respect to Survived')
left_column, right_column = st.columns(2)
with left_column:
   #'Numerical Plot'
    num_feat = st.selectbox(
   'Select Numerical Feature', df.select_dtypes('number').columns)
    fig = px.line(df, x="Date", y=num_feat, title='Flight Cost Trend',color="Date")


    st.plotly_chart(fig, use_container_width=True)
with right_column:
   #'Categorical column'
    cat_feat = st.selectbox(
    'Select Categorical Feature', df.select_dtypes(exclude =   'number').columns)
    fig = fig = px.line(df, x="Date", y="Average Flight Cost", title='Average Flight Cost')
st.plotly_chart(fig, use_container_width=True)

