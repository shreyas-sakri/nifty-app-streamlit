import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import numpy as np

#function to load data
@st.cache_data
def load_data(ticker,start,end):
    data = yf.download(ticker,start=start,end=end)
    return data

#load nifty data
nifty_data = load_data('^NSEI','2014-01-01','2024-06-01')

#function to plot data
def plot_data(data,title):
    fig = px.line(data,x=data.index,y='Close',title=title)
    st.plotly_chart(fig)

#Sreamlit app layout
st.title('NIFTY Index Analysis Around Elections')
st.write("""
    This app shows the NIFTY Index performance before and after the 2014 & 2019 Indian Lok Sabha Elections
         """)
#Show historical data
st.subheader('Historical Nifty Index Data')
st.dataframe(nifty_data.tail())

#Plot data around elections
st.subheader('NIFTY Index around 2014 election')
plot_data(nifty_data['2014-05-01':'2014-07-01'],'NIFTY Index in 2014')

st.subheader('NIFTY Index around 2019 election')
plot_data(nifty_data['2019-05-01':'2019-07-01'],'NIFTY Index in 2019')