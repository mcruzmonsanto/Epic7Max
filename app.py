# app.py
import streamlit as st
from analyzer_engine import GearArchitect

ga = GearArchitect()

st.set_page_config(page_title="E7 Elite Analyzer", layout="centered")

st.title("🛡️ Orbis Elite Analyzer")

# --- BLOQUE 1: METADATOS ---
with st.container():
    col_a, col_b = st.columns(2)
    with col_a:
        gear_type = st.selectbox("Tipo", ["Arma", "Casco", "Pecho", "Collar", "Anillo", "Botas"])
        grade = st.radio("Grado", ["Épico", "Heroico"], horizontal=True)
    with col_b:
        set_name = st.selectbox("Set", ["Speed", "Counter", "Pen", "Destruction", "Lifesteal", "HP"])
        level = st.selectbox("Nivel", [85, 90, 88, 75])

# --- BLOQUE 2: INPUT DE STATS (Estilo Meowyih) ---
st.subheader("🧪 Substats & Procs")
stats = {}
procs = {}

cols = st.columns(2)
substats_list = [
    ('spd', 'Velocidad'), ('atk_p', 'Atk %'), ('cr', 'Crit Rate %'), 
    ('cd', 'Crit Dmg %'), ('hp_p', 'HP %'), ('def_p', 'Def %'),
    ('eff', 'Eficacia %'), ('res', 'Resistencia %')
]

for i, (key, label) in enumerate(substats_list):
    with cols[i % 2]:
        c1, c2 = st.columns([2, 1])
        stats[key] = c1.number_input(label, 0, 350, 0, key=f"val_{key}")
        if level == 85: # Solo pedir procs si es para predecir reforge
            procs[key] = c2.number_input("Rolls", 0, 5, 0, key=f"proc_{key}")

# --- BLOQUE 3: RESULTADOS ---
if st.button("🚀 CALCULAR ANÁLISIS PROFUNDO", use_container_width=True):
    current_score = ga.calculate_score(stats)
    
    st.divider()
    
    # Métricas principales
    m1, m2 = st.columns(2)
    m1.metric("Score Actual", f"{current_score:.1f}")
    
    if level == 85:
        reforge_score = ga.estimate_reforge(stats, procs)
        m2.metric("Potencial Reforge (90)", f"{reforge_score:.1f}")
    
    # Veredicto Estratégico (Lógica Zorathx + Meta 2026)
    st.subheader("💡 Veredicto del Analista")
    if current_score < 45:
        st.error("⚠️ Calidad Baja: No desperdiciar oro. Esta pieza no alcanzará el meta de RTA.")
    elif current_score >= 60:
        st.success(f"🔥 God Roll: Esta pieza es excepcional para un build de {set_name}.")
    
    # Análisis de sinergia
    if stats['spd'] >= 12:
        st.info("🏃 Perfil: Iniciador/Opener. Ideal para unidades que buscan el primer turno.")
