import streamlit as st
import math
from PIL import Image

# Logo
logo = Image.open("logo.png")
st.image(logo, width=200)

# Título
st.title("Calculadora de Tamanho de Amostra")

def calcular_tamanho_amostra(N, margem_erro=0.05, nivel_confianca=0.95, proporcao=0.5):
    z_scores = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
    Z = z_scores.get(nivel_confianca, 1.96)
    n = (Z**2 * proporcao * (1 - proporcao)) / (margem_erro**2)
    n_corrigido = n / (1 + (n / N))
    return math.ceil(n_corrigido)

# Inputs
N = st.number_input("População total (N)", min_value=1, max_value=10_000_000, value=19000, step=100)
margem_erro = st.slider("Margem de erro (%)", min_value=1, max_value=10, value=5) / 100
nivel_confianca_str = st.selectbox("Nível de confiança", options=["90%", "95%", "99%"], index=1)

usar_proporcao_manual = st.radio(
    "Você sabe a proporção esperada da característica que está pesquisando?",
    ("Não sei (usar 50%)", "Sim, quero informar manualmente")
)

if usar_proporcao_manual == "Sim, quero informar manualmente":
    proporcao = st.slider("Informe a proporção esperada (%)", min_value=1, max_value=99, value=50) / 100
else:
    proporcao = 0.5

nivel_confianca = {"90%": 0.90, "95%": 0.95, "99%": 0.99}[nivel_confianca_str]
tamanho_amostra = calcular_tamanho_amostra(N, margem_erro, nivel_confianca, proporcao)

st.subheader("Resultado")
st.write(f"Tamanho da amostra necessário: **{tamanho_amostra}** pessoas")
