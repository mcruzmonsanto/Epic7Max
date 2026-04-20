import streamlit as st
from engine import OrbisArchitectEngine

# Configuración inicial
st.set_page_config(page_title="Orbis Architect Elite", layout="wide")
engine = OrbisArchitectEngine()

# Diseño visual oscuro y limpio
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    div[data-testid="stMetricValue"] { font-size: 2rem; color: #00ffa2 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Orbis Architect Elite V1")
st.caption("Integración: Meowyih + Needlebot + RTAStats + Epic7x")

# --- SECCIÓN 1: METADATOS ---
with st.container():
    c1, c2, c3 = st.columns(3)
    with c1:
        grade = st.selectbox("Grado de la Pieza", ["Épico", "Heroico"])
        set_name = st.selectbox("Set de Equipo", ["Speed", "Counter", "Destruction", "Lifesteal", "HP", "Torrent"])
    with c2:
        level = st.selectbox("Nivel Base", [85, 90, 88, 75])
        enh = st.select_slider("Mejora actual", options=[0, 3, 6, 9, 12, 15], value=15)
    with c3:
        st.info("💡 Consejo: Las piezas Heroicas deben tener GS > 35 en +9 para continuar.")

st.divider()

# --- SECCIÓN 2: INPUT DE STATS ---
st.subheader("🧪 Atributos (+15 o actuales)")
col_s1, col_s2, col_s3, col_s4 = st.columns(4)

with col_s1:
    spd = st.number_input("Velocidad", 0, 30, 0)
    atk_p = st.number_input("Ataque %", 0, 60, 0)
with col_s2:
    hp_p = st.number_input("Vida %", 0, 60, 0)
    def_p = st.number_input("Defensa %", 0, 60, 0)
with col_s3:
    cr = st.number_input("Crit Rate %", 0, 100, 0)
    cd = st.number_input("Crit Dmg %", 0, 350, 0)
with col_s4:
    eff = st.number_input("Eficacia %", 0, 100, 0)
    res = st.number_input("Resistencia %", 0, 100, 0)

# Diccionario de entrada
current_stats = {'spd': spd, 'atk_p': atk_p, 'hp_p': hp_p, 'def_p': def_p, 'cr': cr, 'cd': cd, 'eff': eff, 'res': res}

# --- SECCIÓN 3: RESULTADOS Y ANÁLISIS ---
if st.button("🚀 EJECUTAR ANÁLISIS TÉCNICO", use_container_width=True):
    gs = engine.calculate_gs(current_stats)
    efficiency = engine.calculate_efficiency(current_stats, grade, enh)
    meta_info = engine.get_rta_meta_advice(set_name)
    
    st.divider()
    
    # Dashboard de métricas
    m1, m2, m3 = st.columns(3)
    m1.metric("Gear Score", f"{gs:.1f}")
    m2.metric("Eficiencia", f"{efficiency:.1f}%")
    m3.metric("Potencial", "God Tier" if gs > 65 else "Competitivo" if gs > 50 else "Filler")

    # Veredicto dinámico
    st.subheader("📋 Veredicto del Analista")
    st.write(meta_info)
    
    if enh < 15 and efficiency < 60:
        st.error("⚠️ Según Epic7x: La eficiencia es muy baja. Considera dejar de mejorar para ahorrar recursos.")
    elif gs >= 60:
        st.success("💎 Pieza de nivel Emperador/Leyenda. Prioridad de Reforge nivel 90.")
    else:
        st.warning("📦 Pieza útil para progresión general o unidades de PvE.")
