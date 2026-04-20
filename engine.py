import pandas as pd

class OrbisArchitectEngine:
    def __init__(self):
        # Pesos oficiales de Gear Score (GS)
        self.WEIGHTS = {
            'spd': 2.0, 'cr': 1.6, 'cd': 1.14, 'atk_p': 1, 'hp_p': 1, 
            'def_p': 1, 'eff': 1, 'res': 1, 'atk_f': 0.1, 'hp_f': 0.02, 'def_f': 0.15
        }
        
        # Máximos rolls nivel 85 para calcular Eficiencia (Needlebot Style)
        self.MAX_ROLLS = {
            'spd': 4, 'cr': 5, 'cd': 7, 'atk_p': 8, 'hp_p': 8, 'def_p': 8, 'eff': 8, 'res': 8
        }

    def calculate_gs(self, stats):
        return sum(stats[s] * self.WEIGHTS.get(s, 0) for s in stats)

    def calculate_efficiency(self, stats, grade, enhancement):
        """Calcula qué tan cerca están los rolls del máximo (Lógica Meowyih)"""
        # Un item épico +15 tiene 9 rolls (4 base + 5 mejoras)
        max_possible_rolls = (4 if grade == "Épico" else 3) + (enhancement // 3)
        current_sum_ratios = sum(stats[s] / self.MAX_ROLLS.get(s, 8) for s in stats if stats[s] > 0)
        return (current_sum_ratios / max_possible_rolls) * 100 if max_possible_rolls > 0 else 0

    def get_rta_meta_advice(self, set_name):
        """Basado en Epic7RTAStats 2026"""
        meta = {
            "Speed": "🔥 Tier S: Indispensable para Openers y DPS rápidos.",
            "Counter": "🛡️ Tier A+: Dominante en Bruisers (Mort, Belian).",
            "Destruction": "⚔️ Tier S: Máximo Win Rate en builds de One-shot.",
            "Torrent": "⚠️ Tier Niche: Solo para unidades con poco HP base."
        }
        return meta.get(set_name, "✅ Set balanceado para uso general.")
