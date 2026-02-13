from .base import AprovadorBase

class Supervisor(AprovadorBase):
    "Representa hadler elo 1"
    def processar(self, pedido):
        if pedido.valor <= 500:
            return f"Supervisor aprovou {pedido.descricao}"
        return super().processar(pedido)
    
class Gerente(AprovadorBase):
    "Representa handler elo 2"
    def processar(self, pedido):
        if pedido.valor <= 1000:
            return f"Gerente aprovou {pedido.descricao}"
        return super().processar(pedido)
    
class Diretor(AprovadorBase):
    "Representa Handler elo 3"
    def processar(self, pedido):
        if pedido.valor <= 10000:
            return f"Diretor aprovou {pedido.descricao}"
        return super().processar(pedido)
    
class Ceo(AprovadorBase):
    "Representa handler elo final"
    def processar(self, pedido):
        return f"Ceo aprovou {pedido.descricao}"
