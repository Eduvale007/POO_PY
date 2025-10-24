class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor 
        self.especie = especie


    def apresentar(self):
        print(f'Eu sou o {self.especie} chamado {self.nome}')    



class Gato(Animal):
    def emitir_som(self):
        print('Miau!')


    def arranhar(self):
        print('O gato está arranhando')


class Cachorro(Animal):
    def emitir_som(self):
        print('au au!')

class Elefante(Animal):
    def emitir_som(self):
        print('pruum!')

gato1 = Gato('Felix', 'preto', 'frajola')
gato1.apresentar()
gato1.emitir_som()
gato1.arranhar()

cachorro1 = Cachorro('Arnoold', 'branco', 'caramelo')
cachorro1.apresentar()
cachorro1.emitir_som()

elefante1 = Elefante('jhon', 'cinza', 'dumbo')
elefante1.apresentar()
elefante1.emitir_som()