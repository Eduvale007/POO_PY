class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor 
        self.quartos = quartos
        self.banheiros = banheiros
    
    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')
    
    def mostrar_quartos(self):
        print(f'Essa casa tem {self.quartos} quartos')

    def mostrar_banheiros(self):
        print(f'A casa tem {self.banheiros} banheiros')

    def adicionar_quarto(self, novo_quarto):
        self.quartos += novo_quarto
        print(f'Essa casa tem {self.quartos} quartos')
    
    def pintar(self,nova_cor):
        self.cor = nova_cor
        print(f'A nova cor casa é {self.cor}')


casa1 = Casa('Azul', 4, 2)
casa2 = Casa('Amarelo', 2, 1)

print('Casa 1')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto(2)
casa1.pintar('Rosa')

print('\nCasa 2')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()