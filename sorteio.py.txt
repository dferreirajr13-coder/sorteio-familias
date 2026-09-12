import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Sorteio de Famílias", page_icon="🎉", layout="centered")

# Carregar a planilha
df = pd.read_excel("RELAÇÃO SOMENTE COM OS NOMES.xlsx")

# Cabeçalho com logos
col1, col2 = st.columns([1,1])
with col1:
    st.image("logo_ministerio.png", width=180)
with col2:
    st.image("logo_igreja.png", width=180)

# Título estilizado
st.markdown(
    "<h1 style='text-align: center; color: #d62828;'>🎉 Sorteio de Famílias 🎉</h1>",
    unsafe_allow_html=True
)

# Escolher quantidade
qtd = st.radio("Quantas famílias deseja sortear?", [2,3])

# Botão para sortear
if st.button("Sortear"):
    sorteados = df.sample(n=qtd)
    
    st.markdown(
        "<h2 style='text-align: center; color: #003049;'>Famílias sorteadas:</h2>",
        unsafe_allow_html=True
    )
    
    # Exibir cada família com destaque
    for i, row in sorteados.iterrows():
        nome = row[1]   # coluna com nome
        endereco = row[2] if len(row) > 2 else ""
        st.markdown(
            f"<div style='background-color:#f77f00; padding:15px; margin:10px; border-radius:10px; text-align:center; color:white; font-size:20px; font-weight:bold;'>"
            f"{nome}<br><span style='font-size:16px; font-weight:normal;'>{endereco}</span></div>",
            unsafe_allow_html=True
        )
