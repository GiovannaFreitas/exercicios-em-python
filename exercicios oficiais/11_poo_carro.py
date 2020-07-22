"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível
 no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
 reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
meuFusca.andar(100); # anda 100 quilômetros.
meuFusca.obterGasolina() # Imprime o combustível que resta no tanque."""

class Carro:

    def __init__(self, consumo, combustivel=0):
        self.consumo = consumo
        self.combustivel = combustivel

    def andar(self, distancia):
        if self.combustivel == 0:
            return f"carro sem combustivel"
        else:
            self.andando = True
            self.combustivel -= distancia/8
            return f"combustivel restante: {self.combustivel}L"

    def obter_gasolina(self):
        return f"nivel atual de combustivel: {self.combustivel}L"

    def adicionar_gasolina(self, quantidade):
        self.combustivel += quantidade
        return f"abastecimento efetuado"

meu_fusca = Carro(15)
print(meu_fusca.adicionar_gasolina(20))
print(meu_fusca.andar(100))
print(meu_fusca.obter_gasolina())





