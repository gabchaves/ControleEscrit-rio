import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit import components

# Load the data
file_path = 'Database.csv'
df = pd.read_csv(file_path)

st.set_page_config(layout='wide')
st.title("Dashboard de Clientes")

st.sidebar.title('Filtro de Clientes')

# Carregue sua imagem
background_image = "Fundo.png"  # Substitua pelo caminho correto ou use caminhos relativos

# Adicione a imagem ao fundo usando a biblioteca 'html'
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url("{background_image}") no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

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
