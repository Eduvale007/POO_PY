# Herança multipla e multinivel

# Classe Avo
class Animal:
    def __init__(self, nome):
        self.nome = nome 

#Classes Pai
class Predador(Animal):
    def cacando(sefl):
        print(f'O animal {sefl.nome }  está caçando!')


class Presa(Animal):
     def fugindo(self):
        print(f'O animal {self.nome} sendo caçado!')


#Classes Filho
class Coelho(Presa):
    pass


class Tigre(Predador):
    pass


class Golfinho(Predador, Presa):
    pass 

coelho1 = Coelho('Bunny')
coelho1.fugindo()


tigre1 = Tigre('Leo')
tigre1.cacando()


golfinho1 = Golfinho('Billey')
golfinho1.cacando()



