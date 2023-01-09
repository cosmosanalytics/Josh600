import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
st.title('Josh 600 Actual vs Model')

@st.cache
def loadData():
    s = pd.read_csv('Josh_s.csv', index_col = 0);
    p = pd.read_csv('Josh_p.csv', index_col = 0); 
    return s, p
 
s, p = loadData()
col1, col2 = st.columns(2)
with col1:
    p1 = st.selectbox('Select production plant-generic combination', pd.Series(p.columns).apply(lambda x: x.split('_')[0]).unique())
    fig, ax = plt.subplots(figsize=(20,10))  
    try:
        p[p.columns[p.columns.str.contains(p1)]].plot(ax=ax)
    except:
        pass
    st.pyplot(fig)
with col2:
    s1 = st.selectbox('Select shipment plant-generic combination', pd.Series(s.columns).apply(lambda x: x.split('_')[0]).unique())
    fig, ax = plt.subplots(figsize=(20,10))  
    try:
        s[s.columns[s.columns.str.contains(s1)]].plot(ax=ax)
    except:
        pass
    st.pyplot(fig)
     
