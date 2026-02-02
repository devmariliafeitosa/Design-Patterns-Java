#Essa é a Classe Pai dos Corpos Celestes.
class CorpoCeleste:
    def __init__(self, nome): #Construtor Utilizado para criar o corpo Celeste 
        self.nome = nome


class Planeta(CorpoCeleste): #aqui a classe planeta está Herdando tudo que a ClasseCeleste Possui
    pass


class Lua(CorpoCeleste): #Aqui acontece a mesma coisa que na classe planeta 
    pass


#Aqui Criei uma Classe Pai Para as Roupas 
class RoupaEspacial:
    def __init__(self, tipo):
        self.tipo = tipo


class TrajeEVA(RoupaEspacial): #aqui ela herda de roupa espacial , porém eu utilizei o super para definir um nome fixo
    def __init__(self):
        super().__init__("Roupa Espacial Extraveicular")


# aqui a classe nave pede um nome para poder ser criada e salva o nome 
class Nave:
    def __init__(self, nome):
        self.nome = nome

#essa classe é para criar o astronauta com o nome e o corpo celeste que ele está
class Astronauta:
    def __init__(self, nome, corpo_celeste_atual):
        self.nome = nome
        self.local_atual = corpo_celeste_atual #essa variavel é pra guardar um objeto inteiro do tipo planeta pra poder saber onde o astronauta está