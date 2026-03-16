# 🚀 Atividade Prática: Padrões de Projeto de Software

Este repositório contém a implementação de padrões de projeto voltados para o desacoplamento e a flexibilidade do código. O objetivo desta atividade é aplicar o padrão **Observer**, **State** e o padrão **Strategy** para resolver problemas arquiteturais em cenários de e-commerce.

---

## 👤 Informações do Projeto
* **Instituição:** IFCE - Campus Tauá
* **Curso:** Análise e Desenvolvimento de Sistemas
* **Professor:** Samuel Alves Soares
* **Aluna:** Marília da Silva Feitosa
* **Aluno:** Guilherme Monteiro

---

## 📂 Estrutura de Pastas

```text
Implementacao-04/
├── Observer/
│   ├── main.py
│   ├── produto.py
│   └── observadores.py
└── Strategy/
│   ├── main.py
│   ├── Calculadora.py
│  └── Estrategias.py
├── STATE/
    ├── pedido_state.py
    
```



## 🔔 1. Padrão Observer (Observador)

Cenário: Sistema de Alertas Dinâmicos no E-commerce.
O que foi feito?

Neste exercício, refatorei a classe Produto para que ela não dependesse diretamente das APIs de Marketing, Vendas ou Logística.

- Classe Produto (Publisher): Atua como a fonte de eventos. Ela mantém uma lista de assinantes e os notifica automaticamente sempre que o método set_preco() é chamado.

- Interface ObservadorDePreco: Define o contrato atualizar(produto) para garantir que todos os departamentos interessados saibam como reagir às mudanças.

- Flexibilidade: É possível adicionar ou remover departamentos (como Marketing ou Vendas) em tempo de execução sem alterar o código da classe Produto.

## 🎯 2. Padrão Strategy (Estratégia)

Cenário: Motor de Regras de Frete e Descontos.
O que foi feito?

Substituí uma grande estrutura de if/else por um conjunto de estratégias encapsuladas.

- Interface EstrategiaDeFrete: Define o método calcular(carrinho) que deve ser implementado por qualquer nova transportadora.

- Classes de Estratégia: Cada regra de cálculo (PAC, Sedex, Motoboy) foi isolada em sua própria classe.

- Injeção de Comportamento: A classe CalculadoraDeFrete recebe a estratégia dinamicamente, permitindo que a regra de negócio seja trocada sem que a calculadora precise conhecer a matemática interna de cada frete.

## ⚙️ 3. Padrão State (Estado)

Cenário: Máquina de Estados de um Pedido.
O que foi feito?

Eliminei os complexos blocos de if/else ou switch/case que controlavam o ciclo de vida do pedido.

- Interface EstadoPedido: Define as ações (pagar, despachar, cancelar) que cada estado deve obrigatoriamente implementar.

- Classes de Estado Concretas: Cada classe (ex: EstadoNovo, EstadoEmSeparacao) contém as regras de negócio específicas para aquele momento do pedido.

- Transições Dinâmicas: O objeto Pedido delega as ações para seu estado atual. A transição de um status para outro (ex: de EstadoNovo para EstadoAguardandoPagamento) ocorre internamente, delegando a responsabilidade de "passar o bastão" para o próximo estado, tornando o fluxo de trabalho muito mais organizado e fácil de manter.

## 🚀 Como Executar

O projeto está organizado por pastas. Para testar cada padrão de forma independente:

    Abra o terminal no VS Code.

    Navegue até a pasta do padrão desejado:
    Bash

    # Exemplo para entrar na pasta do Observer
    cd Implementacao-04/Observer

    Execute o arquivo principal:
    Bash

    python main.py

    Siga as instruções que aparecerão no console para interagir com o sistema.
