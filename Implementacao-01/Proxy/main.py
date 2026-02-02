from proxy_imagem import ProxyImagem

def testar_proxy():
    # Aqui eu criei o objeto Proxy. 
    # Repare que no terminal não vai aparecer 'Carregando...' ainda!
    imagem = ProxyImagem("foto_pesada_high_res.jpg")

    print("1. O objeto Proxy foi criado, mas a imagem ainda não está na memória.")
    print("2. Vou esperar 2 segundos antes de exibir...")
    
    import time
    time.sleep(2)

    print("\n3. Agora sim, vou chamar o método exibir() pela primeira vez:")
    imagem.exibir() # Aqui o Proxy vai carregar a imagem real

    print("\n4. Vou chamar o exibir() de novo:")
    imagem.exibir() # Aqui o Proxy já tem a imagem, então será instantâneo!

if __name__ == "__main__":
    testar_proxy()