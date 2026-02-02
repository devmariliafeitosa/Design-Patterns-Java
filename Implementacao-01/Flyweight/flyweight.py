# flyweight.py

class TicketType:
    """
    O Flyweight (Estado Intrínseco):
    Aqui eu criei esta classe para guardar tudo o que se repete em milhares de ingressos.
    Em vez de cada ingresso ter seu próprio 'Rock in Rio' escrito na memória, 
    todos eles vão apontar para uma instância desta classe. Isso economiza muita RAM!
    """
    def __init__(self, evento, local, data, cor):
        self.evento = evento
        self.local = local
        self.data = data
        self.cor = cor

    def exibir(self, id_comprador):
        """
        Este método combina o que é fixo (evento, data) com o que é único (ID do comprador).
        Eu fiz assim para que o objeto compartilhado saiba imprimir os dados do dono do ingresso
        sem precisar guardar o nome do dono dentro de si.
        """
        print(f"Ticket [{self.cor}] - Evento: {self.evento} ({self.data}) | Local: {self.local} | ID: {id_comprador}")


class TicketFactory:
    """
    A Fábrica Flyweight:
    Eu criei esta classe para ser a 'gerente' dos ingressos. 
    A ideia é que ela verifique se um tipo de ingresso (ex: Ouro) já foi criado.
    Se já existir, ela entrega o que está pronto; se não, ela cria um novo.
    """
    # Este dicionário é o meu 'estoque' ou cache de objetos já criados
    _ticket_types = {}

    @classmethod
    def get_ticket_type(cls, evento, local, data, cor):
        """
        Neste método eu verifico a existência do objeto.
        Eu usei uma 'key' (chave) com os dados fixos para saber se aquele tipo é inédito.
        """
        key = (evento, local, data, cor)
        
        if key not in cls._ticket_types:
            # Se não achei no dicionário, eu crio e aviso no console
            print(f"-- Criando novo objeto de memória para a cor: {cor} --")
            cls._ticket_types[key] = TicketType(evento, local, data, cor)
        
        return cls._ticket_types[key]

    @classmethod
    def total_objetos(cls):
        """Criei este método só para provar que a memória está sendo poupada."""
        return len(cls._ticket_types)