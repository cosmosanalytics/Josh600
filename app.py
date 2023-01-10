import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
st.title('Josh 600 Actual vs Model')

@st.cache
def loadData():
    s = pd.read_csv('Josh_s.csv', index_col = 0); s.index = pd.to_datetime(s.index)
    p = pd.read_csv('Josh_p.csv', index_col = 0); p.index = pd.to_datetime(p.index)
    sp = pd.read_csv('Josh_s_perf.csv', index_col = 0);
    pp = pd.read_csv('Josh_p_perf.csv', index_col = 0);     
    return s, p, sp,pp
 
s, p, sp, pp = loadData()
col1, col2 = st.columns(2)
with col1:
    p1 = st.selectbox('Select production plant-generic combination', pd.Series(p.columns).apply(lambda x: x.split('_')[0]).unique())
    fig, ax = plt.subplots(figsize=(10,5))  
    try:
        smape, corrcoef = pp.loc[p1,'corr. coef'].split('_')[0], pp.loc[p1,'corr. coef'].split('_')[1]
        p_plot = p[p.columns[p.columns.str.contains(p1)]]
        ax = p_plot.plot(ax=ax, title='corr. coef. = '+corrcoef+', smape = '+smape)
        ax.axhline(y=np.nanmean(p_plot))
    except:
        pass
    st.pyplot(fig)
with col2:
    s1 = st.selectbox('Select shipment plant-generic combination', pd.Series(s.columns).apply(lambda x: x.split('_')[0]).unique())
    fig, ax = plt.subplots(figsize=(10,5))  
    try:
        smape, corrcoef = sp.loc[s1,'corr. coef'].split('_')[0], sp.loc[s1,'corr. coef'].split('_')[1]
        s[s.columns[s.columns.str.contains(s1)]].plot(ax=ax, title='corr. coef. = '+corrcoef+', smape = '+smape)
    except:
        pass
    st.pyplot(fig)
     
