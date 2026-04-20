# analyzer_engine.py

class GearArchitect:
    def __init__(self):
        # Pesos oficiales de puntuación (Score)
        self.WEIGHTS = {
            'atk_p': 1, 'hp_p': 1, 'def_p': 1, 'eff': 1, 'res': 1,
            'cr': 1.6, 'cd': 1.1, 'spd': 2.0, 'atk_f': 0.1, 'hp_f': 0.02, 'def_f': 0.15
        }
        
        # Incrementos fijos de Reforge (Nivel 85 -> 90)
        # Basado en la lógica de Meowyih: los stats suben según cuántas veces 'prolearon'
        self.REFORGE_MAP = {
            'atk_p': [1, 3, 4, 5, 7, 8], # 0 procs a 5 procs
            'spd': [0, 2, 3, 4, 4, 5],
            'cr': [1, 2, 3, 3, 4, 5],
            'cd': [1, 2, 3, 4, 5, 7],
            # ... resto de stats
        }

    def calculate_score(self, stats):
        return sum(v * self.WEIGHTS.get(k, 0) for k, v in stats.items())

    def estimate_reforge(self, stats, procs):
        """Simula el score final en Nivel 90 basándose en el historial de mejora"""
        reforged_stats = {}
        for s, val in stats.items():
            if val > 0:
                p = procs.get(s, 0)
                bonus = self.REFORGE_MAP.get(s, [1, 2, 3, 4, 5, 7])[p]
                reforged_stats[s] = val + bonus
        return self.calculate_score(reforged_stats)
