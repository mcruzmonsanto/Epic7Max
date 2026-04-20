import streamlit as st
from core import E7Analyzer

st.title("🛡️ Orbis Gear Analyst")

with st.expander("📥 Ingresa Sub-stats de la Pieza"):
    spd = st.number_input("Velocidad", 0, 30, 4)
    atk = st.slider("Ataque %", 0, 50, 0)
    hp = st.slider("Vida %", 0, 50, 0)
    # ... añadir el resto de sliders

if st.button("📊 Analizar Pieza"):
    stats = {'speed': spd, 'atk_pct': atk, 'hp_pct': hp}
    gs = E7Analyzer.calculate_gs(stats)
    role = E7Analyzer.get_role_suggestion(stats)
    
    st.metric("Gear Score", f"{gs:.2f}")
    st.info(f"💡 Rol Recomendado: {role}")
    
    if gs < 45:
        st.error("⚠️ Veredicto Zorathx: EXTRAER / VENDER")
    elif gs > 65:
        st.success("🔥 Veredicto Zorathx: PIEZA ÉPICA - REFORGE!")
