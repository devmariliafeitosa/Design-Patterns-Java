from __future__ import annotations
from abc import ABC, abstractmethod

class EstadoPedido(ABC):
    """Classe base abstrata que dita as regras para todos os estados."""
    
    def __init__(self, pedido: Pedido):
        self.pedido = pedido

    @abstractmethod
    def pagar(self):
        pass

    @abstractmethod
    def despachar(self):
        pass

    @abstractmethod
    def cancelar(self):
        pass

class Pedido:
    def __init__(self):
        self.estado_atual = EstadoNovo(self)

    def alterar_estado(self, novo_estado: EstadoPedido):
        self.estado_atual = novo_estado

    def pagar(self):
        self.estado_atual.pagar()

    def despachar(self):
        self.estado_atual.despachar()

    def cancelar(self):
        self.estado_atual.cancelar()

class EstadoNovo(EstadoPedido):
    def pagar(self):
        print("[Novo] Processando o pagamento...")
    
        self.pedido.alterar_estado(EstadoAguardandoPagamento(self.pedido))

    def despachar(self):
        print("[Novo] ERRO: Não podemos despachar um pedido que nem foi pago!")

    def cancelar(self):
        print("[Novo] Pedido cancelado na hora. Nenhum valor foi cobrado.")
        self.pedido.alterar_estado(EstadoCancelado(self.pedido))


class EstadoAguardandoPagamento(EstadoPedido):
    def pagar(self):
        print("[Aguardando] Pagamento aprovado com sucesso!")
    
        self.pedido.alterar_estado(EstadoEmSeparacao(self.pedido))

    def despachar(self):
        print("[Aguardando] ERRO: Segura aí! O cartão ainda não aprovou.")

    def cancelar(self):
        print("[Aguardando] Pedido cancelado na hora. Estornando limite do cartão.")
        self.pedido.alterar_estado(EstadoCancelado(self.pedido))


class EstadoEmSeparacao(EstadoPedido):
    def pagar(self):
        print("[Em Separação] ERRO: Este pedido já foi pago.")

    def despachar(self):
        print("[Em Separação] Pacote na transportadora! Despachado.")
    
        self.pedido.alterar_estado(EstadoEnviado(self.pedido))

    def cancelar(self):
        print("[Em Separação] AVISO URGENTE: Avisando o estoque para PARAR o pacote!")
        self.pedido.alterar_estado(EstadoCancelado(self.pedido))


class EstadoEnviado(EstadoPedido):
    def pagar(self):
        print("[Enviado] ERRO: Pedido já pago e a caminho.")

    def despachar(self):
        print("[Enviado] ERRO: O pedido já está na rua.")

    def cancelar(self):
        print("[Enviado] ERRO AO CANCELAR: O pacote já saiu. Inicie o processo de Logística Reversa (Devolução).")
        


class EstadoCancelado(EstadoPedido):
    def pagar(self):
        print("[Cancelado] ERRO: Pedido morto não recebe pagamento.")

    def despachar(self):
        print("[Cancelado] ERRO: Pedido morto não é despachado.")

    def cancelar(self):
        print("[Cancelado] O pedido já está cancelado.")

if __name__ == "__main__":
    print(" CENÁRIO 1: Fluxo Feliz ")
    pedido1 = Pedido()
    pedido1.pagar()       # Novo -> Aguardando
    pedido1.pagar()       # Aguardando -> Em Separacao
    pedido1.despachar()   # Em Separacao -> Enviado
    pedido1.cancelar()    # Tenta cancelar um pedido já enviado (Logística Reversa)

    print("\n CENÁRIO 2: Cancelando na Separação")
    pedido2 = Pedido()
    pedido2.pagar()       # Novo -> Aguardando
    pedido2.pagar()       # Aguardando -> Em Separacao
    pedido2.cancelar()    # Avisa o estoque para parar o pacote!