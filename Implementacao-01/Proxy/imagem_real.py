import time
from interface_imagem import Imagem

class ImagemDisco(Imagem):
    """
    O Objeto Real:
    Eu criei esta classe para representar o arquivo pesado. 
    Assim que ela é instanciada, ela já tenta carregar do disco (demorado).
    """
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self._carregar_do_disco()

    def _carregar_do_disco(self):
        print(f"Carregando {self.nome_arquivo} do disco... (Operação Pesada)")
        # Simula o delay de 1 segundo que o professor pediu
        time.sleep(1)

    def exibir(self):
        print(f"Exibindo imagem: {self.nome_arquivo}")