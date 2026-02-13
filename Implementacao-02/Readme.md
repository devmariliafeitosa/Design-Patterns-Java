# 🚀 Implementação 02: Design Patterns Comportamentais

Este repositório contém a implementação prática dos padrões de projeto **Chain of Responsibility** e **Command**, desenvolvida para a disciplina de Padrões de Projetos.

**Professor:** Samuel Alves

---

## 👥 Equipe e Responsabilidades

| Padrão de Projeto | Desenvolvedor(a) |
| :--- | :--- |
| **Chain of Responsibility** | Marilia Feitosa |
| **Command** | Guilherme Monteiro |

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Ambiente:** VS Code

---

## 🏗️ Estrutura do Projeto

O projeto está dividido em dois módulos principais:

### 1. Chain of Responsibility (Sistema de Aprovação)
Localizado em: `Chain-Of-Responsability/Sistema_Aprovacao/`
Implementa uma cadeia hierárquica onde uma despesa é passada entre Supervisor, Gerente, Diretor e CEO até ser aprovada conforme o limite de cada cargo.

* **src/base.py:** Define a abstração do Handler.
* **src/aprovadores.py:** Contém os elos concretos da corrente.
* **src/pedido.py:** Representa o objeto de dados da compra.

### 2. Command (Projeto Remoto)
Localizado em: `COMMAND/projeto_remoto/`
Implementa o encapsulamento de solicitações como objetos, permitindo que um controle remoto execute ações em diferentes receptores (como luzes ou aparelhos) de forma desacoplada.

* **comandos.py:** Interface e comandos concretos.
* **receptores.py:** Classes que contêm a lógica de negócio real.
* **invoker.py:** O disparador dos comandos (Controle Remoto).

---

## 🚀 Como Executar

### Importante: Uso do Terminal no VS Code
Devido à natureza interativa dos sistemas (especialmente o Chain), **não utilize a aba "SAÍDA" (Output)** do VS Code para digitar. Ela é apenas leitura.

**Siga estes passos:**
1. Abra um **Novo Terminal** (`Ctrl + '`).
2. Navegue até a pasta do padrão desejado.
3. Execute o comando:
   ```bash
   python main.py