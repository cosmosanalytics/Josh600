import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
st.title('Josh 600 Actual vs Model')

@st.cache
def loadData():
    s = pd.read_csv('Josh_s.csv', index_col = 0); s.index = pd.to_datetime(s.index)
    p = pd.read_csv('Josh_s.csv', index_col = 0); p.index = pd.to_datetime(p.index)
    return s, p
 
s, p = loadData()
col1, col2 = st.columns(2)
with col1:
    pl = st.selectbox('Select production plant-generic combination', pd.Series(p.columns).apply(lambda x: x.split('_')[0]).unique())
    fig, ax = plt.subplots(figsize=(20,10))  
    try:
        p[p.columns[p.columns.str.contains(pl)]].plot(ax=ax)
    except:
        pass
    st.pyplot(fig)
with col2:
    sl = st.selectbox('Select shipment plant-generic combination', pd.Series(s.columns).apply(lambda x: x.split('_')[0]).unique())
    fig, ax = plt.subplots(figsize=(20,10))  
    try:
        s[s.columns[s.columns.str.contains(sl)]].plot(ax=ax)
    except:
        pass
    st.pyplot(fig)
     
