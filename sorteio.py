import streamlit as st
import pandas as pd
 
st.set_page_config(
page_title="Sorteio de Famílias",
page_icon="🎉",
layout="centered"
)
 
df = pd.read_excel("FAMILIAS.xlsx")
df = df.dropna(how="all")
 
col1, col2 = st.columns(2)
 
with col1:
st.image("logo_ministerio.png", width=150)
 
with col2:
st.image("logo_igreja.png", width=150)
 
st.title("🎉 Sorteio de Famílias")
 
qtd = st.selectbox(
"Quantidade de famílias a sortear",
[2, 3]
)
 
if st.button("SORTEAR"):
 
sorteados = df.sample(n=qtd)
 
st.success("Famílias sorteadas")
 
for _, row in sorteados.iterrows():
 
if len(row) > 1:
nome = str(row.iloc[1])
else:
nome = ""
 
if len(row) > 2:
endereco = str(row.iloc[2])
else:
endereco = ""
 
st.markdown(
f"""
<div style="
background-color:#f77f00;
padding:20px;
margin:10px;
border-radius:15px;
text-align:center;
color:white;">
<h2>{nome}</h2>
<p>{endereco}</p>
</div>
""",
unsafe_allow_html=True
)
