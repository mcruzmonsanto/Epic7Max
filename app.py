# app.py
import streamlit as st
from analyzer_engine import OrbisArchitectPro

engine = OrbisArchitectPro()

st.set_page_config(page_title="E7 Gear Architect Pro", layout="wide")

# --- CSS PERSONALIZADO PARA MÓVILES ---
st.markdown("""
    <style>
    .stSelectbox, .stNumberInput { margin-bottom: -10px; }
    .reportview-container .main .block-container { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ E7 Gear Architect Pro")

# --- SECCIÓN 1: METADATOS DEL EQUIPO ---
with st.expander("📦 Identificación de la Pieza", expanded=True):
    c1, c2, c3 = st.columns(3)
    with c1:
        gear_type = st.selectbox("Tipo de Pieza", ["Arma", "Casco", "Armadura", "Collar", "Anillo", "Botas"])
        set_type = st.selectbox("Set", ["Speed", "Counter", "Destruction", "Lifesteal", "HP", "Immunity", "Penetration", "Torrent"])
    with c2:
        grade = st.selectbox("Grado", ["EPIC", "HEROIC"])
        level = st.selectbox("Nivel Base", [85, 88, 90, 75])
    with c3:
        enhancement = st.slider("Mejora (+)", 0, 15, 15, step=3)
        main_stat = st.selectbox("Stat Principal", ["Atk %", "HP %", "Def %", "Speed", "Crit Rate", "Crit Dmg", "Eff", "Res"])

# --- SECCIÓN 2: SUB-STATS (INPUT TIPO NEEDLEBOT) ---
st.subheader("🧪 Sub-Atributos")
col_s1, col_s2, col_s3, col_s4 = st.columns(4)

with col_s1:
    spd = st.number_input("Velocidad", 0, 30, 0)
    atk = st.number_input("Atk %", 0, 60, 0)
with col_s2:
    cr = st.number_input("Crit Rate %", 0, 100, 0)
    cd = st.number_input("Crit Dmg %", 0, 350, 0)
with col_s3:
    hp = st.number_input("HP %", 0, 60, 0)
    df = st.number_input("Def %", 0, 60, 0)
with col_s4:
    eff = st.number_input("Eff %", 0, 100, 0)
    res = st.number_input("Res %", 0, 100, 0)

stats = {'spd': spd, 'atk': atk, 'cr': cr, 'cd': cd, 'hp': hp, 'def': df, 'eff': eff, 'res': res}

# --- SECCIÓN 3: ANÁLISIS PROFUNDO ---
if st.button("🚀 EJECUTAR ANÁLISIS TÉCNICO", use_container_width=True):
    gs = engine.get_gear_score(stats)
    eff_roll = engine.calculate_efficiency(stats, grade, enhancement)
    reforge_gs = engine.get_reforge_potential(stats, gear_type) if level == 85 else gs
    
    st.divider()
    
    # Dashboard de Métricas
    m1, m2, m3 = st.columns(3)
    m1.metric("Gear Score Actual", f"{gs:.1f}")
    m2.metric("Eficiencia de Rolls", f"{eff_roll:.1f}%")
    m3.metric("Potencial Nivel 90", f"{reforge_gs:.1f} GS")

    # Lógica de Veredicto Zorathx
    st.subheader("💡 Análisis de Rol y Meta")
    
    if grade == "HEROIC" and gs < 40 and enhancement < 9:
        st.error("⚠️ ALERTA: Rolls bajos para pieza Heroica. No gastar más recursos.")
    elif gs >= 65:
        st.success(f"🔥 PIEZA TOP-TIER: Excelente para set de {set_type}. Prioridad máxima de reforge.")
    
    # Sugerencia de Héroe (Basado en Set + Stats)
    if set_type == "Speed" and spd > 12:
        st.info("🎯 Destinatario sugerido: Openers (Lídica, Peira) o Fast DPS (Celine).")
    elif set_type == "Counter" and hp > 15:
        st.info("🎯 Destinatario sugerido: Bruisers de contraataque (Mort, Abigail).")
