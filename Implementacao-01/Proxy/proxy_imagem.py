from interface_imagem import Imagem
from imagem_real import ImagemDisco

class ProxyImagem(Imagem):
    """
    O Proxy:
    Eu criei esta classe para 'enganar' o sistema. Ela guarda o nome do arquivo,
    mas não carrega nada agora. Ela só vai instanciar a ImagemDisco de verdade
    quando alguém chamar o método exibir().
    """
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.imagem_real = None # Começa vazio para não gastar memória

    def exibir(self):
        # Aqui eu faço a mágica do 'Carregamento sob Demanda':
        if self.imagem_real is None:
            print(f"Proxy: Opa, primeira vez que pedem para exibir {self.nome_arquivo}. Vou carregar agora!")
            self.imagem_real = ImagemDisco(self.nome_arquivo)
        
        # Depois de carregado (ou se já estava carregado), eu exibo
        self.imagem_real.exibir()