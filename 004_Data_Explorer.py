import streamlit as st
import io
import pandas as pd
import plotly.express as px
import os

#set page
st.set_page_config(
    layout='wide',
    initial_sidebar_state='expanded',
    page_icon='WERT',
    page_title='Data Explorer')

#Load data
path = os.path.dirname(__file__)
path = os.path.join(path,"iris.data")

st.header('Data Exploreer')

sidebr = st.sidebar.file_uploader('Upload dataset',['csv','.data','*lsx','txt'])

