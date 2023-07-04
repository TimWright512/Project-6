import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header('Data viewer')
show_manuf_1k_ads = st.checkbox('Include manufacturers with less than 1000 ads')
if not show_manuf_1k_ads:
    df = df.groupby('manufacturer').filter(lambda x: len(x) > 1000)

st.dataframe(df)
st.header('Vehicle Types by their Condition')
st.write(px.histogram(df, x='type', color='condition'))
st.header('Bar Chart of `Manufacturer` and the amount of `Days Listed`')

st.bar_chart(df,
                      x='manufacturer',
                      y='days_listed',
                      width=0,
                      height=0,
                      use_container_width=True
)
st.subheader("Age vs Condition")
df = pd.read_csv('vehicles_us.csv')
fig = px.scatter(
    df,
    x="condition",
    y="car_age",
    color="car_age",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)