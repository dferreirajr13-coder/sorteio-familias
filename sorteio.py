import streamlit as st
import pandas as pd 
st.set_page_config(
page_title="Sorteio de Famílias",
page_icon="🎉",
layout="centered"
)
 
df = pd.read_excel("FAMILIAS.xlsx")
 
col1, col2 = st.columns(2)
 
with col1:
st.image("logo_ministerio.png", width=150)
 
with col2:
st.image("logo_igreja.png", width=150)
 
st.title("🎉 Sorteio de Famílias")
 
qtd = st.radio(
"Quantidade de famílias para sortear",
[2, 3]
)
 
if st.button("SORTEAR"):
 
sorteados = df.sample(n=qtd)
 
st.success("Famílias Sorteadas")
 
for _, row in sorteados.iterrows():
 
st.write("✅", row.iloc[1])
