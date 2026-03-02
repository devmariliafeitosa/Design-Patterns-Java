class Musica:
    def __init__(self, nome, artista, favorita=False):
        self.nome = nome
        self.artista = artista
        self.favorita = favorita

    def __str__(self):
        icone = "[FAVORITA]" if self.favorita else "[NORMAL]"
        return f"{icone} {self.nome} - {self.artista}"