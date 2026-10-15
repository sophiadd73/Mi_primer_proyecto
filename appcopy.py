import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\sxphi\OneDrive\Desktop\Programacion\streamlit\YARDAS_PASOS_DATOS_TICS.xlsx", index_col=0)

st.header("5 columnas")
st.dataframe(df.head())

st.header("Estadistica Descriptiva")
st.dataframe(df.describe())

df.columns = [c.lower().replace(' ', '_') for c in df.columns]

col1, col2 = st.columns(2)

with col1: 
    #Pases completos
    fig, ax = plt.subplots()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigote\n de pases completos")
    st.pyplot(fig)

with col2: 
    #Yardas totales
    fig, ax = plt.subplots()
    ax.boxplot(df['yardas_totales'])
    st.header("Diagrama de caja y bigote\n de yardas totales")
    st.pyplot(fig)