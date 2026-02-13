from abc import ABC, abstractmethod

# Interface (Contrato)
class Comando(ABC):
    @abstractmethod
    def executar(self):
        pass
        
    @abstractmethod
    def desfazer(self):
        pass

# Comando Concreto para Luz
class ComandoLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def executar(self):
        self.luz.ligar()

    def desfazer(self):
        self.luz.desligar()

# Comando Concreto para Portão
class ComandoPortao(Comando):
    def __init__(self, portao):
        self.portao = portao

    def executar(self):
        self.portao.abrir()

    def desfazer(self):
        self.portao.fechar()