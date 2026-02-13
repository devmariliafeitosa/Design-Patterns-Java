# main.py
from src.pedido import PedidoCompra
from src.aprovadores import Supervisor, Gerente, Diretor, Ceo

def executar():
    # 1. Criando os objetos dos aprovadores
    sup = Supervisor()
    ger = Gerente()
    diret = Diretor()
    ana_ceo = Ceo()
    
    # 2. Montando a corrente (Hierarquia)
    # Supervisor -> Gerente -> Diretor -> CEO
    sup.definir_proximo(ger).definir_proximo(diret).definir_proximo(ana_ceo)

    print("="*40)
    print("   SISTEMA INTERATIVO DE COMPRAS")
    print("="*40)
    print("Digite 'sair' no nome do produto para encerrar.\n")

    while True:
        # 3. Entrada de dados pelo usuário
        nome_produto = input("Nome do produto: ")
        
        if nome_produto.lower() == 'sair':
            print("\nEncerrando sistema... Até logo!")
            break
            
        try:
            valor_produto = float(input(f"Valor de '{nome_produto}': R$ "))
        except ValueError:
            print(" Erro: Por favor, digite um valor numérico válido.\n")
            continue

        # 4. Criando o objeto do pedido com os dados digitados
        novo_pedido = PedidoCompra(nome_produto, valor_produto)
        
        # 5. Iniciando o processo pelo primeiro elo (Supervisor)
        print("-" * 30)
        resultado = sup.processar(novo_pedido)
        print(resultado)
        print("-" * 30 + "\n")

if __name__ == "__main__":
    executar()