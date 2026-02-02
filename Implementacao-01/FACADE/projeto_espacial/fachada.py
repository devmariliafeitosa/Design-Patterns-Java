from subsistemas import Planeta, TrajeEVA, Nave, Astronauta

#Simulação que a estação já tem uma nave e roupas prontas no estoque
class CentralDeControleFacade:
    def __init__(self):
        self.nave_da_missao = Nave("Apollo 11")
        self.roupa_padrao = TrajeEVA()

#Define a única ação que o usuário (Cliente) pode fazer.
    def realizar_lancamento(self, nome_astronauta, nome_destino):
        origem = Planeta("Terra")
        
        #aqui prepara a origem sabendo que ele sai da terra
        destino = Planeta(nome_destino)
        
        #e aqui prepara o destino
        astronauta = Astronauta(nome_astronauta, origem)
        
       
        relatorio = (
            f"O astronauta de nome {astronauta.nome} "
            f"vestiu a {self.roupa_padrao.tipo}, "
            f"entrou na nave de nome {self.nave_da_missao.nome} "
            f"e partiu da origem {astronauta.local_atual.nome} "
            f"para o destino {destino.nome}."
        )
        
        return relatorio