# Sistema de Escola
class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status


    def apresentar(self):
        print(f'Meu nome é {self.nome}') 


    def verificar_status(self):
        print(f'Status: {"ATIVO" if self.status else "INATIVO"}')   

class Aluno(Escola):
    def __init__(self, nome, idade, ano, status):
        super().__init__(nome, idade, status)
        self.ano = ano

    
    def apresentar(self):
        super().apresentar()
        print('Eu sou um aluno da escola') # a funcao do filho sempre sobrepoem o pai, caso queira usar a funcao do pai utilize o "super"


class Professor(Escola):
    def __init__(self, nome, idade, materia, status):
        super().__init__(nome, idade, status)
        self.materia = materia


    def apresentar(self):
        super().apresentar()
        print('Eu sou um professor da escola') 


class Assistente(Escola):
    def __init__(self, nome, idade, bloco, status):
        super().__init__(nome, idade, status)
        self.bloco = bloco
    

    def apresentar(self):
        super().apresentar()
        print('Eu sou um(a) assistente da escola') 

a1 = Aluno(nome='Marcos', idade=12, ano=8, status=True)
p1 = Professor(nome='Roberto', idade=34, materia='Geometria', status=True)
as1 = Assistente(nome='Ana Maria', idade=29, bloco='Bloco C', status=False)

a1.apresentar()

