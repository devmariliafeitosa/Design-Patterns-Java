#base

from abc import ABC, abstractmethod

class AprovadorBase(ABC):
    """Representa o handler no padrão"""

    def __init__(self):
        self.proximo_aprovador = None

    def definir_proximo(self, proximo):
        "Operação: set_next. Conecta os elos um ao outro"
        self.proximo_aprovador = proximo
        return proximo
    
    @abstractmethod
    def processar(self, pedido):
        "Operação handle lógica de repasse"
        if self.proximo_aprovador:
            return self.proximo_aprovador.processar(pedido)
        return f"Ninguém aprovou  {pedido.descricao}."