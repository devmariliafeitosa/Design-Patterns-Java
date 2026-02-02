# 🚀 Atividade Prática: Padrões de Projeto de Software

Este repositório contém a implementação de três padrões de projeto estruturais. O objetivo desta atividade é aplicar conceitos de otimização, controle de acesso e simplificação de interfaces em cenários reais.

---

## 👤 Informações do Projeto
* **Instituição:** IFCE - Campus Tauá
* **Semestre:** 2º Semestre - Análise e Desenvolvimento de Sistemas
* **Professor:** Samuel Alves Soares
* **Alunos:** 
   * Marília da Silva Feitosa
  * Guilherme Monteiro de Sousa

---

## 📂 Estrutura de Pastas

```text
padroesprojeto/
└── Implementacao-01/
    ├── Facade/
    │   └── projeto_espacial/
    │       ├── fachada.py
    │       ├── main.py
    │       └── subsistemas.py
    ├── Flyweight/
    │   ├── flyweight.py
    │   └── main.py
    └── Proxy/
        ├── interface_imagem.py
        ├── imagem_real.py
        ├── proxy_imagem.py
        └── main.py
```
## 🏛️ 1. Padrão Facade (Fachada)
**Cenário:** Simulação de um sistema de controle de missão espacial.

### O que fizemos aqui?
Neste exercício, utilizamos uma **Fachada** chamada `CentralDeControleFacade` para gerenciar a complexidade de um lançamento espacial. O sistema possui diversos subsistemas (Nave, Traje, Planeta, Astronauta), e sem a fachada, o cliente teria que configurar cada um deles manualmente.

* **Classe `CentralDeControleFacade`**: Eu criei esta classe para ser o ponto único de interação. Ela já deixa a Nave (Apollo 11) e o Traje (EVA) prontos no estoque.
* **Simplificação**: O usuário só precisa dizer o nome do astronauta e o destino. A fachada cuida de instanciar a origem (Terra), o destino e o astronauta, gerando um relatório completo.
* **Por que usamos?** Para que a `main.py` não precise importar todas as classes de `subsistemas.py`. Isso deixa o código do cliente muito mais limpo e fácil de usar.



---

## 🎟️ 2. Padrão Flyweight (Peso-Pena)
**Cenário:** Gerenciamento de memória para a venda de 100.000 ingressos.

### O que fizemos aqui?
O desafio era evitar que o computador travasse ao criar milhares de objetos quase idênticos.

* **Classe `TicketType`**: Aqui eu guardei o que se repete (Evento, Local, Data e Cor). Isso é o que chamamos de **Estado Intrínseco**.
* **Classe `TicketFactory`**: Criei esta fábrica para garantir que, se já existir um ingresso da cor "Ouro", o sistema reutilize o mesmo objeto em vez de criar um novo.
* **Resultado**: Conseguimos vender 100 mil ingressos, mas a memória do computador só precisou guardar **3 objetos reais**.



---

## 🖼️ 3. Padrão Proxy (Procurador)
**Cenário:** Carregamento "sob demanda" de imagens pesadas do disco.

### O que fizemos aqui?
Implementamos um "atravessador" para evitar que imagens grandes sejam carregadas na memória sem necessidade.

* **Classe `ProxyImagem`**: Ela funciona como um escudo. Ela guarda o nome do arquivo, mas só instancia a classe `ImagemDisco` (que é pesada e tem delay) quando o método `exibir()` é clicado pela primeira vez.
* **Lazy Loading**: O carregamento só acontece "na hora H". Se o usuário nunca pedir para ver a imagem, o sistema nunca gasta processamento com ela.
* **Cache**: Após o primeiro carregamento, o Proxy guarda a imagem real para que as próximas exibições sejam instantâneas.



---

## 🚀 Como Executar

O projeto está dividido na pasta `Implementacao-01`. Para rodar cada um:

1. Abra o terminal no VS Code.
2. Navegue até a pasta do padrão desejado:
   ```bash
   # Exemplo para entrar no Facade
   cd Implementacao-01/Facade/projeto_espacial
   ```
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```