class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')
    
    def promover(self, novo_cargo):
        self.cargo = novo_cargo
        print(f'{self.nome} foi promovido(a) para a nova função de {novo_cargo}')

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando idade de {self.idade} para {nova_idade}')   
        else:
            print('A nova idade tem que ser maior que a anterior')     

colaborador1 = Pessoa('Ana', 36, 'Assistente Junior') 
colaborador2 = Pessoa('Carlos', 45, 'Dev junior')       

colaborador2.informacoes()
colaborador1.informacoes()
colaborador1.promover('Dev junior')
colaborador1.informacoes()