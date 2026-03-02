from abc import ABC, abstractmethod
from musica import Musica


class IteradorDeMusicas(ABC):

    @abstractmethod
    def tem_proximo(self) -> bool:
        pass

    @abstractmethod
    def proximo(self) -> Musica:
        pass


class IteradorSequencial(IteradorDeMusicas):

    def __init__(self, musicas):
        self._musicas = musicas
        self._posicao = 0

    def tem_proximo(self) -> bool:
        return self._posicao < len(self._musicas)

    def proximo(self) -> Musica:
        if self.tem_proximo():
            musica_atual = self._musicas[self._posicao]
            self._posicao += 1
            return musica_atual
        return None


class IteradorFavoritas(IteradorDeMusicas):

    def __init__(self, musicas):
        self._musicas = musicas
        self._posicao = 0

    def tem_proximo(self) -> bool:
        while self._posicao < len(self._musicas):
            if self._musicas[self._posicao].favorita:
                return True
            self._posicao += 1
        return False

    def proximo(self) -> Musica:
        if self.tem_proximo():
            musica_atual = self._musicas[self._posicao]
            self._posicao += 1
            return musica_atual
        return None