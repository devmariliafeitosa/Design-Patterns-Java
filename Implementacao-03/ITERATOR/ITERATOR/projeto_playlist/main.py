import sys
sys.stdout.reconfigure(encoding='utf-8')

from musica import Musica
from playlist import Playlist


if __name__ == "__main__":

    minha_playlist = Playlist()

   
    minha_playlist.adicionar_musica(Musica("Quarta Cadeira", "Matheus & Kauan", favorita=True))
    minha_playlist.adicionar_musica(Musica("Ao Vivo e a Cores", "Matheus & Kauan"))
    
    minha_playlist.adicionar_musica(Musica("Infiel", "Marília Mendonça", favorita=True))
    minha_playlist.adicionar_musica(Musica("Supera", "Marília Mendonça"))
    
    minha_playlist.adicionar_musica(Musica("Novo Eu", "Henrique & Juliano", favorita=True))
    minha_playlist.adicionar_musica(Musica("Hábito de Comprometido", "Henrique & Juliano", favorita=True))

    print("--- MODO SEQUENCIAL ---")
    iterador_normal = minha_playlist.criar_iterador_sequencial()

    while iterador_normal.tem_proximo():
        print(iterador_normal.proximo())

    print("\n--- MODO FAVORITAS ---")
    iterador_favs = minha_playlist.criar_iterador_favoritas()

    while iterador_favs.tem_proximo():
        print(iterador_favs.proximo())