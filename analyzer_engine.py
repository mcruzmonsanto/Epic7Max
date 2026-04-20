# analyzer_engine.py

class OrbisArchitectPro:
    def __init__(self):
        # Rangos oficiales extraídos de OnStove (Nivel 85)
        self.ROLL_DATA = {
            'EPIC': {'min': 4, 'max': 8, 'spd_max': 5, 'cr_max': 5, 'cd_max': 7},
            'HEROIC': {'min': 3, 'max': 7, 'spd_max': 4, 'cr_max': 4, 'cd_max': 6}
        }
        
        # Pesos de Gear Score (GS) y WSS
        self.WEIGHTS = {
            'atk': 1, 'hp': 1, 'def': 1, 'eff': 1, 'res': 1,
            'cr': 1.6, 'cd': 1.14, 'spd': 2.0
        }

    def calculate_efficiency(self, stats, grade, enhancement):
        """
        Calcula la eficiencia basada en el grado y nivel de mejora.
        Lógica: (Suma de rolls actuales / Suma de rolls máximos teóricos)
        """
        max_possible = (4 if grade == 'EPIC' else 3) + (enhancement // 3)
        # Aproximación de eficiencia de rolls individuales
        total_efficiency = sum([stats[s] / self.ROLL_DATA[grade].get(f"{s}_max", 8) for s in stats if stats[s] > 0])
        return (total_efficiency / max_possible) * 100

    def get_gear_score(self, stats):
        return sum(stats[s] * self.WEIGHTS.get(s, 0) for s in stats)

    def get_reforge_potential(self, stats, gear_type):
        """Predice el GS final en Nivel 90"""
        # La velocidad sube +2 a +4, los stats % suben de 7% a 9% usualmente
        bonus = 0
        for s, v in stats.items():
            if v > 0:
                if s == 'spd': bonus += 4
                elif s in ['atk', 'hp', 'def', 'eff', 'res']: bonus += 7
                elif s == 'cr': bonus += 4
                elif s == 'cd': bonus += 5
        return self.get_gear_score(stats) + bonus
