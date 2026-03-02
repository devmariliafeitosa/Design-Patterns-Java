from mediator import ChatRoom
from user import User

sala_de_chat = ChatRoom()

user1 = User(sala_de_chat, "Alice")
user2 = User(sala_de_chat, "Bob")
user3 = User(sala_de_chat, "Carlos")

sala_de_chat.add_user(user1)
sala_de_chat.add_user(user2)
sala_de_chat.add_user(user3)

user1.send("Olá pessoal!")
