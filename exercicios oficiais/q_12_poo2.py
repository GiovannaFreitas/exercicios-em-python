class Conta_investimento:

    def __init__(self,saldo_inial,taxa_juros):
        self.saldo_inial = saldo_inial
        self.taxa_juros = taxa_juros

    
    def adicionejuros(self):
        res = self.saldo_inial * self.taxa_juros
        res += self.saldo_inial
        return res
        


c1 = Conta_investimento(1000, 0.2)
print(c1.adicionejuros())