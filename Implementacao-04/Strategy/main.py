from Calculadora import CalculadoraDeFrete
from Estrategias import FretePAC, FreteSedex, FreteMotoboy

def main():
    peso = float(input("Digite o peso do pacote (kg): "))
    print("\nEscolha o frete:")
    print("1 - PAC: R$ 15,00 + R$ 1,00/kg | 2 - Sedex: R$ 30,00 + R$ 2,50/kg | 3 - Motoboy: R$ 20,00")
    escolha = input("Opção: ")

    opcoes = {
        '1': FretePAC(),
        '2': FreteSedex(),
        '3': FreteMotoboy()
    }

    estrategia = opcoes.get(escolha)

    if estrategia:
        calculadora = CalculadoraDeFrete(estrategia)
        valor = calculadora.calcular(peso)
        print(f"\nValor final do frete: R$ {valor:.2f}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()