import streamlit as st
from datetime import datetime
from datetime import date

def diferenca_em_anos(data1, data2):
    diferenca_anos = data1.year - data2.year
    if (data1.month, data1.day) < (data2.month, data2.day):
        diferenca_anos -= 1
    return diferenca_anos


st.write("Cálculo entre datas")

col1, col2 = st.columns(2)


with col1:
    data_inicio = st.date_input("Selecione uma data de início:", date.today())

with col2:
    data_fim = st.date_input("Selecione uma data fim:", date.today())



if st.button("Calcular:"):
    diferença = data_fim - data_inicio
    if diferenca_em_anos(data_fim, data_inicio) < 1:
        st.write(f"{diferença.days} dias")
    else:
        anos = diferenca_em_anos(data_fim, data_inicio)
        dias_r = diferença.days - (anos * 365)
        st.write(f"{anos} anos e {dias_r} dias.")