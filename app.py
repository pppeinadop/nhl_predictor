import streamlit as st

st.set_page_config(
    page_title="NHL Predictor",
    page_icon="🏒",
    layout="wide"
)

st.title("🏒 NHL Predictor")

st.markdown("---")

st.subheader("Proyecto de Predicción NHL")

st.write("Bienvenido al sistema de predicción de partidos de NHL.")

col1, col2 = st.columns(2)

with col1:
    st.selectbox(
        "Equipo Local",
        ["Boston Bruins", "Colorado Avalanche", "Dallas Stars"]
    )

with col2:
    st.selectbox(
        "Equipo Visitante",
        ["Edmonton Oilers", "Vegas Golden Knights", "New York Rangers"]
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