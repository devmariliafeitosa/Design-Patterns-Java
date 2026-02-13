# 🛡️ Sistema de Aprovação - Chain of Responsibility

Este projeto foi desenvolvido para demonstrar o padrão de projeto comportamental **Chain of Responsibility**.

## 🎯 Objetivo
Evitar o acoplamento entre o remetente de uma solicitação de compra e quem a processa, permitindo que múltiplos objetos (Supervisor, Gerente, Diretor, CEO) tenham a chance de tratar a solicitação.

## 🧱 Papel das Classes no Padrão

1.  **`AprovadorBase` (Handler):**
    - Classe abstrata que define o método `definir_proximo` (para montar a corrente) e a estrutura do método `processar`.
    - **Operação Destacada:** `processar()`. No padrão, ela representa o mecanismo de delegação. Se o objeto atual não resolve, ele "empurra" a tarefa para o sucessor.

2.  **`Supervisor, Gerente, Diretor e CEO` (Concrete Handlers):**
    - São os elos da corrente. Cada um conhece apenas sua regra de negócio (limite de valor).
    - Se o pedido estiver dentro do limite, ele encerra a execução. Caso contrário, invoca o comportamento da classe pai para passar adiante.

3.  **`PedidoCompra` (Request):**
    - Objeto simples que carrega os dados (valor e descrição). Ele é o "pacote" que viaja pela corrente.

## ⚙️ Operações Principais
- **`definir_proximo(proximo)`**: No padrão, esta é a operação de **Linker/Setup**. Ela permite que a hierarquia seja configurada dinamicamente no arquivo `main.py`, sem que o Supervisor precise saber quem é o Gerente dentro do código.

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para baixar e executar o sistema em sua máquina:

### 1. Clonar o Repositório
Abra o terminal ou prompt de comando e digite:
```bash
git clone 
(https://github.com/devmariliafeitosa/Design-Patterns-Java/tree/main/Implementacao-02)
```
### 2. Acessar a Pasta
Entre no diretório do projeto:
```bash
cd sistema_aprovacao
```

### 3. Executar o Projeto
Para rodar o projeto, utilize o comando:
```bash
python main.py
```