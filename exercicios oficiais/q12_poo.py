'''Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros.
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método 
adicioneJuros() cinco vezes e imprime o saldo resultante.'''



class ContaInvestimento:


    def __init__(self, saldo_inicial, taxa_juros=0.1):
        self.saldo_inicial = saldo_inicial
        self.taxa_juros = taxa_juros


    def adicionarjuros(self):
        res = self.saldo_inicial * self.taxa_juros
        res += self.saldo_inicial
        return res



c1 = ContaInvestimento(1000)
print(c1.adicionarjuros())

    