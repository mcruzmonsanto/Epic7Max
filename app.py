# app.py
import streamlit as st
from analyzer_engine import OrbisArchitectEngine

# Inicializar el motor
engine = OrbisArchitectEngine()

st.set_page_config(page_title="Orbis Architect Pro", layout="wide")

# Estilo para móviles (Android)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Orbis Architect Pro")
st.caption("Análisis de Equipamiento basado en Meta 2026")

# Sección de Entrada de Datos
with st.container():
    st.subheader("📥 Atributos de la Pieza (+15)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        spd = st.number_input("Velocidad", 0, 30, 4, step=1)
        atk = st.number_input("Ataque %", 0, 60, 0)
    with col2:
        hp = st.number_input("Vida %", 0, 60, 0)
        def_pct = st.number_input("Defensa %", 0, 60, 0)
    with col3:
        cr = st.number_input("Prob. Crítica %", 0, 100, 0)
        cd = st.number_input("Daño Crítico %", 0, 350, 0)

# Diccionario de stats para el motor
input_stats = {'spd': spd, 'atk': atk, 'hp': hp, 'def': def_pct, 'crit_rate': cr, 'crit_dmg': cd}

# Ejecutar Análisis al presionar botón
if st.button("🔍 ANALIZAR PIEZA", use_container_width=True):
    gs = engine.get_gear_score(input_stats)
    eff = engine.get_efficiency(input_stats)
    verdict = engine.analyze_meta_fit(input_stats)
    
    # Dashboard de Resultados Estilo App Moderna
    st.divider()
    m1, m2 = st.columns(2)
    m1.metric("Gear Score (GS)", f"{gs:.1f}")
    m2.metric("Roll Efficiency", f"{eff:.1f}%")
    
    st.info(f"**Veredicto de Meta:** {verdict}")
    
    # Recomendación basada en lógica Zorathx
    if gs < 50:
        st.warning("⚠️ Recomendación: Esta pieza no cumple los estándares para PvP. Considerar como 'Placeholder' en PvE.")
    else:
        st.success("✨ Recomendación: Pieza de alto potencial. Priorizar para Reforge de Nivel 90.")
