from abc import ABC, abstractmethod

class EstrategiaDeFrete(ABC):
    @abstractmethod
    def calcular(self, peso):
        pass

class FretePAC(EstrategiaDeFrete):
    def calcular(self, peso):
        return 15.0 + (1.0 * peso)

class FreteSedex(EstrategiaDeFrete):
    def calcular(self, peso):
        return 30.0 + (2.5 * peso)

class FreteMotoboy(EstrategiaDeFrete):
    def calcular(self, peso):
        return 20.0 