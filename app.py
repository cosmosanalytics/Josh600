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

# def 
 
s, p, sp, pp = loadData()
col1, col2 = st.columns(2)
with col1:
    p1 = st.selectbox('Select production plant-generic combination', pd.Series(p.columns).apply(lambda x: x.split('_')[0]).unique())
    fig, ax = plt.subplots(figsize=(10,5))  
    try:
        smape, corrcoef = pp.loc[p1,'corr. coef'].split('_')[0], pp.loc[p1,'corr. coef'].split('_')[1]
        p_plot = p[p.columns[p.columns.str.contains(p1)]]
        
        p_plot['col0 avg'] = p_plot[p_plot.columns[0]].mean(); p_plot['col0 std'] = p_plot[p_plot.columns[0]].std()
        p_plot['col0 avg+std'] = p_plot['col0 avg'] + p_plot['col0 avg']; p_plot['col0 avg-std'] = p_plot['col0 avg'] - p_plot['col0 std']
        p_plot['col1 avg'] = p_plot[p_plot.columns[1]].mean(); p_plot['col1 std'] = p_plot[p_plot.columns[1]].std()
        p_plot['col1 avg+std'] = p_plot['col1 avg'] + p_plot['col1 avg']; p_plot['col1 avg-std'] = p_plot['col1 avg'] - p_plot['col1 std']
        
        p_plot[p_plot.columns[0]].plot(ax=ax, color='blue'); 
        p_plot[['col0 avg','col0 avg+std','col0 avg-std']].plot(ax=ax, color='blue', linestyle = '--', alpha=0.5, legend=None)
        p_plot[p_plot.columns[1]].plot(ax=ax, color='orange'); 
        p_plot[['col0 avg','col1 avg+std','col1 avg-std']].plot(ax=ax, color='orange', linestyle = '--', alpha=0.5, legend=None)
        ax.set_title('hihiicorr. coef. = '+corrcoef+', smape = '+smape)

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
     
