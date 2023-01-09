import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
st.title('Josh 600 Actual vs Model')

@st.cache
def loadData():
    s = pd.read_csv('Josh_s.csv', index_col = 0)
    p = pd.read_csv('Josh_s.csv', index_col = 0)
    return s, p
 
s, p = loadData()
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots(figsize=(20,10))
    st.title('Production')
    gp = st.multiselect('Select plant-generic combination', p.columns)
    st.write(gp.values)
    p[gp].plot()
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots(figsize=(20,10))
    st.title('Shipment')
    gp = st.multiselect('Select plant-generic combination', s.columns)
    s[gp].plot()
    st.pyplot(fig)
     
