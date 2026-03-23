from abc import ABC, abstractmethod

# 1. A INTERFACE DO VISITANTE (A "Operação Externa")

class Visitor(ABC):
    """
    Interface base para qualquer 'Visitante'. 
    Um visitante é uma classe que contém operações que seriam aplicadas 
    aos produtos, mas que foram extraídas para não inchar as classes de dados.
    Se amanhã precisarmos calcular o frete, basta criar um 'FreteVisitor' 
    que implementa esta mesma interface.
    """
    
    @abstractmethod
    def visitar_alimento(self, alimento: 'Alimento'):
        pass

    @abstractmethod
    def visitar_eletronico(self, eletronico: 'Eletronico'):
        pass

    @abstractmethod
    def visitar_bebida_alcoolica(self, bebida: 'BebidaAlcoolica'):
        pass

# 2. O VISITANTE CONCRETO (A Regra de Negócio de Impostos)

class CalculadoraImpostoVisitor(Visitor):
    """
    Visitante específico para calcular impostos.
    Aqui ficam todas as regras fiscais. O Produto não sabe calcular imposto, 
    ele apenas 'recebe' este visitante e deixa que o visitante faça o cálculo.
    """
    
    def __init__(self):
        self.total_impostos = 0.0

    def visitar_alimento(self, alimento: 'Alimento'):
        # Regra 1: Alimentos são isentos (0% de imposto)
        imposto = alimento.preco * 0.0
        self.total_impostos += imposto
        print(f"[Imposto] {alimento.nome}: Isento (R$ {imposto:.2f})")

    def visitar_eletronico(self, eletronico: 'Eletronico'):
        # Regra 2: Eletrônicos possuem 15% de imposto
        imposto = eletronico.preco * 0.15
        self.total_impostos += imposto
        print(f"[Imposto] {eletronico.nome}: 15% (R$ {imposto:.2f})")

    def visitar_bebida_alcoolica(self, bebida: 'BebidaAlcoolica'):
        # Regra 3: Bebidas Alcoólicas possuem 40% de imposto
        imposto = bebida.preco * 0.40
        self.total_impostos += imposto
        print(f"[Imposto] {bebida.nome}: 40% (R$ {imposto:.2f})")


# 3. A INTERFACE DOS ELEMENTOS (Os Produtos)

class Produto(ABC):
    """
    Interface base dos produtos.
    A única obrigação do Produto agora é ter o método aceitar (accept).
    Ele NÃO precisa saber calcular imposto, frete ou etiqueta.
    """
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def aceitar(self, visitor: Visitor):
        """
        Método crucial do padrão Visitor (Double Dispatch).
        O produto recebe o visitante e chama o método correspondente ao seu próprio tipo.
        """
        pass


# 4. OS ELEMENTOS CONCRETOS (Dados puros, sem regras de negócio misturadas)

class Alimento(Produto):
    def aceitar(self, visitor: Visitor):
        # "Oi Visitante, eu sou um Alimento. Aplique a sua regra para Alimentos em mim."
        visitor.visitar_alimento(self)

class Eletronico(Produto):
    def aceitar(self, visitor: Visitor):
        # "Oi Visitante, eu sou um Eletrônico. Aplique a sua regra para Eletrônicos em mim."
        visitor.visitar_eletronico(self)

class BebidaAlcoolica(Produto):
    def aceitar(self, visitor: Visitor):
        # "Oi Visitante, sou uma Bebida Alcoólica. Aplique a sua regra para Bebidas em mim."
        visitor.visitar_bebida_alcoolica(self)


# 5. A ESTRUTURA DE OBJETOS (O Carrinho de Compras)

class CarrinhoDeCompras:
    """
    Mantém a lista de produtos e facilita a passagem do visitante por todos eles.
    """
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto: Produto):
        self.itens.append(produto)

    def calcular_tributacao(self):
        """
        Instancia o visitante de impostos e passa ele por cada produto do carrinho.
        """
        calculadora_imposto = CalculadoraImpostoVisitor()
        
        print("INICIANDO AUDITORIA FISCAL")
        for item in self.itens:
            # Cada item 'aceita' o visitante, gerando o cálculo correto para seu tipo
            item.aceitar(calculadora_imposto)
            
        print("-" * 35)
        print(f"TOTAL DE IMPOSTOS A PAGAR: R$ {calculadora_imposto.total_impostos:.2f}")
        print("-" * 35)


# 6. O CLIENTE (Executando o sistema)

if __name__ == "__main__":
    carrinho = CarrinhoDeCompras()
    
    # Adicionando produtos (Os produtos são apenas DADOS, não possuem lógica fiscal)
    carrinho.adicionar_item(Alimento("Arroz 5kg", 25.00))
    carrinho.adicionar_item(Eletronico("Smartphone", 2000.00))
    carrinho.adicionar_item(BebidaAlcoolica("Vinho Tinto", 100.00))
    carrinho.adicionar_item(Alimento("Feijão 1kg", 8.00))

    # Executa a operação externa (Visitor) sobre os elementos
    carrinho.calcular_tributacao()