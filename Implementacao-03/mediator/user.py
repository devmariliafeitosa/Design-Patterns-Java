class User:
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    def send(self, message):
        print(f"--- {self.name} enviando: {message} ---")
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"[{self.name} recebeu]: {message}")