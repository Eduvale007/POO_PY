class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

    def apresentar(self):
        print(f'Olá, o meu nome é {self.nome} e tenho {self.idade}')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo
    

    def trabalhar(self):
        print(f'{self.nome} está trabalhando como {self.cargo}')


class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo
    

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'Olá {self.nome} a sua compra de {valor_compra} foi Aprovada! Seu Saldo Atual é de: {self.saldo}')
        else:
            print(f'Olá {self.nome}! O seu Saldo  foi insuficiente')


f1 = Funcionario('Maria', 38, 'Gerente de contas')
f1.trabalhar()


c1 = Cliente('Athur', 16, 200)
c1.comprar(80)