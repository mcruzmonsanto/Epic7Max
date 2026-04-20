# analyzer_engine.py
class OrbisArchitectEngine:
    def __init__(self):
        # Umbrales máximos oficiales (Nivel 85) para cálculo de Eficiencia
        self.MAX_ROLLS = {
            'atk': 8, 'hp': 8, 'def': 8, 'spd': 4,
            'crit_rate': 5, 'crit_dmg': 7, 'eff': 8, 'res': 8
        }

    def get_gear_score(self, stats):
        """Calcula el Gear Score (GS) con pesos de optimizador profesional"""
        return (
            stats.get('atk', 0) + stats.get('hp', 0) + stats.get('def', 0) +
            stats.get('eff', 0) + stats.get('res', 0) +
            (stats.get('crit_rate', 0) * 1.6) +
            (stats.get('crit_dmg', 0) * 1.14) +
            (stats.get('spd', 0) * 2.0)
        )

    def get_efficiency(self, stats):
        """Calcula la eficiencia de los rolls (Lógica Needlebot)"""
        actual_rolls = sum(stats.get(k, 0) / self.MAX_ROLLS[k] for k in self.MAX_ROLLS if stats.get(k, 0) > 0)
        # Se divide por el número de sub-stats presentes para promediar
        substats_count = len([v for v in stats.values() if v > 0])
        return (actual_rolls / 4) * 100 if substats_count > 0 else 0

    def analyze_meta_fit(self, stats):
        """Determina si la pieza encaja en el meta de GvG (Lógica Fribbels)"""
        gs = self.get_gear_score(stats)
        spd = stats.get('spd', 0)
        
        if spd >= 16: return "🚀 GOD-SPEED (Opener Meta)"
        if gs >= 65: return "🏆 COMPETITIVE (High-End PvP)"
        if stats.get('hp', 0) >= 16 and stats.get('def', 0) >= 12: return "🛡️ BRUISER/TANK CORE"
        return "📦 PVE / PROGRESSION"
