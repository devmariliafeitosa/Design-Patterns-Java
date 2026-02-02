from fachada import CentralDeControleFacade

if __name__ == "__main__":
    print(">>> SISTEMA DA ESTAÇÃO DE CONTROLE INICIADO <<<\n")

    # 1. Instancia da Fachada
    sistema_de_viagem = CentralDeControleFacade()

    # aqui o usuario define quem vai e para onde vai 
    nome = "Marcos Pontes"
    onde_vai = "Lua"

   
    resultado = sistema_de_viagem.realizar_lancamento(nome, onde_vai)


    print(resultado)
    print("\n>>> FIM DA OPERAÇÃO <<<")