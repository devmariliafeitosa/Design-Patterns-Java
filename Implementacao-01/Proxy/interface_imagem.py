from abc import ABC, abstractmethod

# Aqui eu criei uma Classe Abstrata para servir de Interface.
# Eu fiz isso para garantir que tanto o Proxy quanto a Imagem Real 
# tenham o método exibir(). É como um contrato.
class Imagem(ABC):
    @abstractmethod
    def exibir(self):
        pass