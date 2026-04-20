# core.py
class E7Analyzer:
    @staticmethod
    def calculate_gs(stats):
        """Calcula el Gear Score estándar con pesos de Fribbels/OnStove"""
        weights = {
            'atk_pct': 1, 'hp_pct': 1, 'def_pct': 1, 
            'eff': 1, 'res': 1,
            'crit_rate': 1.6, 'crit_dmg': 1.1, 'speed': 2
        }
        return sum(stats.get(s, 0) * weights[s] for s in weights)

    @staticmethod
    def get_role_suggestion(stats):
        """Lógica Zorathx para asignar roles"""
        gs = E7Analyzer.calculate_gs(stats)
        if stats.get('speed', 0) > 12 and stats.get('eff', 0) > 10:
            return "Opener / Control (Lidica, Peira)"
        if stats.get('hp_pct', 0) > 15 and stats.get('def_pct', 0) > 10:
            return "Tank / Mitigador (Ras SC, Mort)"
        return "DPS / Bruiser"
