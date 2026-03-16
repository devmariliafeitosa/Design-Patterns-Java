class CalculadoraDeFrete:
    def __init__(self, estrategia=None):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, peso):
        if not self.estrategia:
            return 0.0
        return self.estrategia.calcular(peso)