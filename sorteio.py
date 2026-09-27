import streamlit as st
import pandas as pd
 
st.set_page_config(
page_title="Sorteio de Famílias",
page_icon="🎉",
layout="centered"
)
 
# Carregar planilha
df = pd.read_excel("familias.xlsx")
 
# Remover linhas vazias
df = df.dropna(how="all")
 
# Logos
col1, col2 = st.columns(2)
 
with col1:
st.image("logo_ministerio.png", width=150)
 
with col2:
st.image("logo_igreja.png", width=150)
 
st.title("🎉 Sorteio de Famílias")
 
qtd = st.selectbox(
"Quantidade de famílias:",
[2, 3]
)
 
if st.button("SORTEAR"):
 
sorteados = df.sample(n=qtd)
 
st.success("Famílias Sorteadas")
 
for _, row in sorteados.iterrows():
 
nome = str(row.iloc[1]) if len(row) > 1 else ""
 
endereco = ""
if len(row) > 2:
endereco = str(row.iloc[2])
 
st.markdown(
f"""
<div style="
background:#f77f00;
padding:20px;
margin:10px;
border-radius:15px;
text-align:center;
color:white;
font-size:24px;
font-weight:bold;
">
{nome}<br>
<span style="font-size:16px;">
{endereco}
</span>
</div>
""",
unsafe_allow_html=True
)
