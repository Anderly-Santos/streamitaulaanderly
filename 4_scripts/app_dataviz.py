import streamlit as st
import pandas as pd
import plotly.express as px

# titulo aplicação
st.write('''**Futebol APP**''')

st.sidebar.header('Escolha os times')

df = pd.read_csv('../1_bases_tratadas/dadostratados.csv', sep=';', encoding='utf-8')

times = df['home_team_name'].drop_duplicates()
escolha_time = st.sidebar.selectbox("Escolha um time",times)

df2 = df[df['home_team_name']==escolha_time]

fig = px.box(df2, x='home_ppg')
st.plotly_chart(fig)

fig2 = px.histogram(df2.home_ppg)
st.plotly_chart(fig2)

fig3 = px.scatter(df2,'home_ppg','over_25_percentage_pre_match')
st.plotly_chart(fig3)

fig4 = px.pie(df2, 'placar')
st.plotly_chart(fig4)
