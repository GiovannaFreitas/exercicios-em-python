'''Classe Bomba de Combustível: Faça um programa 
completo utilizando classes e 
métodos que:

Possua uma classe chamada bombaCombustível, 
com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o 
valor a ser abastecido e 
mostra a quantidade de litros que foi colocada no
veículo
abastecerPorLitro( ) – método onde é informado a 
quantidade em litros de combustível 
e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
combustível total na bomba.'''


class Bombacombustivel:


    def __init__(self, tipo_combustivel, valor_litro, quant_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quant_combustivel = quant_combustivel

    
    def abastecer_por_valor(self, valor):
        resultado = valor / self.valor_litro
        self.quant_combustivel -= resultado
        return f'Valor pago R${valor}, quantidade abastecida: {resultado:.2f}'

    def abastecer_por_litro(self, litros):
        valor_total = litros * self.valor_litro
        self.quant_combustivel -= litros
        return f'Valor Total {valor_total}, quantidade litros {litros}'


    def alterar_valor(self, valor):
        self.valor_litro = valor


    def alterar_tipo_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel


    def alterar_quantidade_combustivel(self, quant_combustivel):
        self.quant_combustivel = quant_combustivel





p1=Bombacombustivel('gasolina', 3.65, 100)
print(p1.abastecer_por_valor(20))
p1.alterar_valor(4)
print(p1.abastecer_por_litro(15))
print(f'quantidade total restante na bomba {p1.quant_combustivel}')
