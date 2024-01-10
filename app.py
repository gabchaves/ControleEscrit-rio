import pandas as pd
import streamlit as st
from streamlit import components

# Load the data
file_path = 'Database.csv'
df = pd.read_csv(file_path)

st.set_page_config(layout='wide')
st.title("Dashboard de Clientes")

st.sidebar.title('Filtro de Clientes')

# Filtro nome:

filtro_Nome = st.sidebar.multiselect(
    'Nome',
    df['Nome'].unique(),
)

if filtro_Nome:
    df = df[df['Nome'].isin(filtro_Nome)]

# Filtro Nº do processo:

filtro_Texto = st.sidebar.text_input('Número do processo')

if filtro_Texto:
    df = df[df['Número do processo'].astype(str).str.contains(filtro_Texto)]

# Abas

aba1, aba2, aba3 = st.tabs(['Nome', 'Nº do Proceso', 'Data'])

with aba1:
    st.dataframe(df)
