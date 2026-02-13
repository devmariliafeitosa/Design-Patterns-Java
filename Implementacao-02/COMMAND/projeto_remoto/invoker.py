class ControleRemoto:
    def __init__(self):
        self.historico_undo = [] # Pilha para desfazer
        self.historico_redo = [] # Pilha para refazer

    def pressionar_botao(self, comando):
        # 1. Executa o comando
        comando.executar()
        
        # 2. Guarda no histórico de Undo
        self.historico_undo.append(comando)
        
        # 3. Limpa o Redo sempre que fazemos algo novo, perdemos o futuro "refazer"
        self.historico_redo.clear()

    def desfazer_ultimo(self):
        if not self.historico_undo:
            print("Nada para desfazer")
            return

        # Tira da pilha de Undo
        comando = self.historico_undo.pop()
        
        # Executa o inverso
        print(f"[UNDO] Desfazendo ação")
        comando.desfazer()
        
        # Joga para a pilha de Redo caso queira se arrepender de ter desfeito
        self.historico_redo.append(comando)

    def refazer_ultimo(self):
        if not self.historico_redo:
            print("Nada para refazer")
            return

        # Tira da pilha de Redo
        comando = self.historico_redo.pop()
        
        # Executa novamente
        print(f"[REDO] Refazendo ação")
        comando.executar()
        
        # Joga de volta para o Undo
        self.historico_undo.append(comando)