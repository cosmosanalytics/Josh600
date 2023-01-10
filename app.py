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

def ps_plot(ps):
    fig, ax = plt.subplots(figsize=(10,5))
    ps['col0 avg'] = ps[ps.columns[0]].mean(); ps['col0 std'] = ps[ps.columns[0]].std()
    ps['col0 avg+std'] = ps['col0 avg'] + ps['col0 avg']; ps['col0 avg-std'] = ps['col0 avg'] - ps['col0 std']
    ps['col1 avg'] = ps[ps.columns[1]].mean(); ps['col1 std'] = ps[ps.columns[1]].std()
    ps['col1 avg+std'] = ps['col1 avg'] + ps['col1 avg']; ps['col1 avg-std'] = ps['col1 avg'] - ps['col1 std']

    ps[ps.columns[0]].plot(ax=ax, color='blue', legend=True); 
    ps[['col0 avg','col0 avg+std','col0 avg-std']].plot(ax=ax, color='blue', linestyle = '--', alpha=0.5, legend=None)
    ps[ps.columns[1]].plot(ax=ax, color='orange', legend=True); 
    ps[['col0 avg','col1 avg+std','col1 avg-std']].plot(ax=ax, color='orange', linestyle = '--', alpha=0.5, legend=None)
    ax.set_title('corr. coef. = '+corrcoef+', smape = '+smape) 
    st.pyplot(fig)
 
s, p, sp, pp = loadData()
col1, col2 = st.columns(2)
with col1:
    p1 = st.selectbox('Select production plant-generic combination', pd.Series(p.columns).apply(lambda x: x.split('_')[0]).unique())  
    try:
        smape, corrcoef = pp.loc[p1,'corr. coef'].split('_')[0], pp.loc[p1,'corr. coef'].split('_')[1]
        ps_plot(p[p.columns[p.columns.str.contains(p1)]])
    except:
        pass   
with col2:
    s1 = st.selectbox('Select shipment plant-generic combination', pd.Series(s.columns).apply(lambda x: x.split('_')[0]).unique())
    try:
        smape, corrcoef = sp.loc[s1,'corr. coef'].split('_')[0], sp.loc[s1,'corr. coef'].split('_')[1]
        ps_plot(s[s.columns[s.columns.str.contains(s1)]])
    except:
        pass
    
