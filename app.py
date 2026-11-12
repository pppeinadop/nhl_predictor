import streamlit as st
import requests

st.set_page_config(
    page_title="NHL Predictor",
    page_icon="🏒",
    layout="wide"
)

# Obtener equipos desde la API NHL
url = "https://api-web.nhle.com/v1/standings/now"
response = requests.get(url)
data = response.json()

teams = sorted(
    [team["teamName"]["default"] for team in data["standings"]]
)

st.title("🏒 NHL Predictor")

st.markdown("---")

st.subheader("Proyecto de Predicción NHL")

st.write("Bienvenido al sistema de predicción de partidos de NHL.")

col1, col2 = st.columns(2)

with col1:
    local = st.selectbox(
        "Equipo Local",
        teams
    )

with col2:
    visitante = st.selectbox(
        "Equipo Visitante",
        teams
    )

st.button("Generar Predicción")

st.markdown("---")

st.metric(
    label="Probabilidad Equipo Local",
    value="60%"
)

st.metric(
    label="Probabilidad Equipo Visitante",
    value="40%"
)