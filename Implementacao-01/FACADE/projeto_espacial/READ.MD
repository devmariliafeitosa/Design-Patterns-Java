o arquivo subsistemas.py tem toda a complexidade (Nave, Roupas, Planetas...).
Se o main tivesse que configurar tudo isso, o código ia ficar muito grande e difícil de mexer."

O Facade.py resolve isso agindo como um gerente. Ele esconde essa complexidade e dá um comando simples: eu só passo quem vai e pra onde vai. A parte de preparar a nave ele faz sozinho.
O main não precisa se preocupar com nada. Eu posso trocar a nave ou a roupa lá na fábrica, e não preciso mudar nenhuma vírgula no código principal, porque ele só manda 'lançar'.

