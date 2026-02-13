# pedido

class PedidoCompra:
    "Representa a solicitação que será analisada."

    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor