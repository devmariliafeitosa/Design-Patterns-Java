from produto import Produto
from observadores import DepartamentoMarketing, DepartamentoVendas

def main():
    nome_produto = input("Digite o nome do produto: ")
    preco_inicial = float(input("Digite o preço inicial: "))
    
    produto = Produto(nome_produto, preco_inicial)

    print("\nQuais departamentos deseja inscrever?")
    if input("Inscrever Marketing? (s/n): ").lower() == 's':
        marketing = DepartamentoMarketing()
        produto.adicionar_observador(marketing)
    
    if input("Inscrever Vendas? (s/n): ").lower() == 's':
        vendas = DepartamentoVendas()
        produto.adicionar_observador(vendas)

    print("-" * 30)
    novo_preco = float(input(f"Digite o novo preço para {produto.nome}: "))
    produto.set_preco(novo_preco)

if __name__ == "__main__":
    main()