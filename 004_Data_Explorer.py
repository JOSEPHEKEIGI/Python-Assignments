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

st.sidebar.header('Data Explorer')

#Load data
# path = os.path.dirname(__file__)
# path = os.path.join(path,"iris.data")



data = st.sidebar.file_uploader('Upload dataset',['csv','.data','*lsx','txt'])



if data is not None:
    df = pd.read_csv(data, sep=',',header=None)
    df.columns = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width','Species']     
    st.header('Sample of Data')
    st.write(df.head(5))    
    st.write()

    cols1, cols2 = st.columns(2)

    with cols1:
        st.subheader("Average Sepal of each species")
        Avg_sepal_length = df.groupby( "Species" )['Sepal_length'].sum()
        st.write(Avg_sepal_length)

    with cols2:
        fig = px.scatter(x= df['Sepal_length'], y = df['Sepal_width'])

        fig.show()
  
