import streamlit as st
import pandas as pd

@st.cache
def loadData():
    s = pd.read_csv('Josh_s.csv', index_col = 0)
    p = pd.read_csv('Josh_s.csv', index_col = 0)
    sp = pd.read_csv('Josh_s_perf.csv', index_col = 0)
    pp = pd.read_csv('Josh_p_perf.csv', index_col = 0)
    return s, p, sp, pp
  
s, p, sp, pp = loadData()
st.write(s)
