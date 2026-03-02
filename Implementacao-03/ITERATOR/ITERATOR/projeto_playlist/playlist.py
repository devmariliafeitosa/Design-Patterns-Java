from iterador import IteradorSequencial, IteradorFavoritas


class Playlist:

    def __init__(self):
        self._lista_interna = []

    def adicionar_musica(self, musica):
        self._lista_interna.append(musica)

    def criar_iterador_sequencial(self):
        return IteradorSequencial(self._lista_interna)

    def criar_iterador_favoritas(self):
        return IteradorFavoritas(self._lista_interna)