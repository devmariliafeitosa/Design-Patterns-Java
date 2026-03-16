from abc import ABC, abstractmethod

class ObservadorDePreco(ABC):
    @abstractmethod
    def atualizar(self, produto):
        pass

class DepartamentoMarketing(ObservadorDePreco):
    def atualizar(self, produto):
        print(f"[Marketing] Notificado! Preço do {produto.nome} mudou para R${produto.preco}")

class DepartamentoVendas(ObservadorDePreco):
    def atualizar(self, produto):
        print(f"[Vendas] Notificado! Preço do {produto.nome} mudou para R${produto.preco}")