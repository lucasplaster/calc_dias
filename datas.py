import streamlit as st
from datetime import datetime
from datetime import date

st.write("Cálculo entre datas")

col1, col2 = st.columns(2)


with col1:
    data_inicio = st.date_input("Selecione uma data de início:", date.today())

with col2:
    data_fim = st.date_input("Selecione uma data fim:", date.today())



if st.button("Calcular:"):
    diferença = data_fim - data_inicio
    st.write(f"{diferença.days} dias")

