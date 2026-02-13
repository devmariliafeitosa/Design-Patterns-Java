from receptores import Luz, Portao
from comandos import ComandoLuz, ComandoPortao
from invoker import ControleRemoto

if __name__ == "__main__":
    # 1. Cria os aparelhos
    luz_sala = Luz()
    portao_garagem = Portao()

    # 2. Cria os comandos 
    # aqui passei os aparelhos para dentro dos comandos
    cmd_luz = ComandoLuz(luz_sala)
    cmd_portao = ComandoPortao(portao_garagem)

    # 3. Cria o Controle
    controle = ControleRemoto()

    print("1. AÇÕES NORMAIS")
    controle.pressionar_botao(cmd_luz)    # Liga a luz
    controle.pressionar_botao(cmd_portao) # Abre o portão

    print("\n 2. TESTANDO DESFAZER (UNDO)")
    controle.desfazer_ultimo() # Deve fechar o portão
    controle.desfazer_ultimo() # Deve desligar a luz

    print("\n 3. TESTANDO REFAZER (REDO)")
    controle.refazer_ultimo()  # Deve ligar a luz de novo
    controle.refazer_ultimo()  # Deve abrir o portão de novo