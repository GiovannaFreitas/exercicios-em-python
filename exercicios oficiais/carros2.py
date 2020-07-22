class Carros:

    def __init__(self,marca, combustivel=0, andando=False):
        self.marca = marca
        self.combustivel = combustivel
        self.andando = andando

    def andar(self, km):
        if self.combustivel == 0:
            return f'Carro sem combustível'
        else:
            self.andando = True
            return f'Combustível restante {self.combustivel - (km/4)}L'

    def parar_andar(self):
        if not self.andando:
            return f'O carro já está parado'
        else:
            self.andando = False
            return f'O carro parou'
    

    def obter_gasolina(self):
        return f'Quantidade atual: {self.combustivel}L'

    def add_gasolina(self, quantidade):
        if self.andando:
            return f'O carro não pode abastecer andando'
        else:
            self.combustivel += quantidade
            return f'Abastecimento efetuado com sucesso'

 #pra executar só se eu pedir   
if __name__ == '__main__':

    c1 = Carros('Fusca', 25)
    print(c1.andar(50))
    c1.parar_andar()
    print(c1.add_gasolina(15))
    print(c1.obter_gasolina())
