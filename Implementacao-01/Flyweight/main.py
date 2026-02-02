# main.py
import random
from flyweight import TicketFactory

def executar_vendas():
    """
    Aqui é onde eu simulo a agência vendendo os ingressos.
    O objetivo é gerar 100.000 vendas sem travar o computador.
    """
    cores = ["Ouro", "Prata", "Bronze"]
    ingressos_vendidos = [] # Aqui eu guardo as referências de cada venda
    total_vendas = 100000

    print(f"Iniciando venda de {total_vendas} ingressos...\n")

    for i in range(total_vendas):
        # Sorteio uma cor para garantir que o código teste os 3 tipos pedidos
        cor_sorteada = random.choice(cores)
        
        # Aqui eu chamo a Fábrica. Eu não dou 'new' no TicketType direto,
        # eu peço para a fábrica me dar o objeto compartilhado.
        tipo = TicketFactory.get_ticket_type(
            "Rock in Rio 2026", 
            "Parque Olímpico", 
            "20/09/2026", 
            cor_sorteada
        )
        
        # O ID do comprador é o dado 'único'. 
        # Eu mantenho ele aqui na Main para não 'sujar' o objeto compartilhado.
        id_unico = f"COMPRADOR {i+1}"
        
        # Guardo o par (objeto compartilhado, id único) na minha lista de vendas
        ingressos_vendidos.append((tipo, id_unico))

    print("\n" + "="*50)
    print(f"Vendas concluídas: {len(ingressos_vendidos)}")
    # Aqui eu mostro que, apesar de 100 mil vendas, a memória só tem 3 objetos reais.
    print(f"Objetos REAIS em memória: {TicketFactory.total_objetos()}")
    print("="*50)
    
    # Imprimindo os 10 primeiros para mostrar que a data e o ID estão aparecendo
    print("\nExemplo dos 10 primeiros ingressos (comprovante):")
    for i in range(10):
        tipo, id_comprador = ingressos_vendidos[i]
        tipo.exibir(id_comprador)

if __name__ == "__main__":
    executar_vendas()