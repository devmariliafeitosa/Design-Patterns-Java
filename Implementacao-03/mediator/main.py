from mediator import ChatRoom
from user import User

# 1. Criamos o Mediador (a Sala)
sala_de_chat = ChatRoom()

# 2. Criamos os usuários passando a sala como referência
user1 = User(sala_de_chat, "Alice")
user2 = User(sala_de_chat, "Bob")
user3 = User(sala_de_chat, "Carlos")

# 3. Registramos os usuários na sala
sala_de_chat.add_user(user1)
sala_de_chat.add_user(user2)
sala_de_chat.add_user(user3)

# 4. Comunicação
user1.send("Olá pessoal!")
# Bob e Carlos devem receber, Alice não.