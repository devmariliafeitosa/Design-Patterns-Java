class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self._observadores = []

    def adicionar_observador(self, obs):
        self._observadores.append(obs)

    def remover_observador(self, obs):
        if obs in self._observadores:
            self._observadores.remove(obs)

    def set_preco(self, valor):
        self.preco = valor
        for obs in self._observadores:
            obs.atualizar(self)