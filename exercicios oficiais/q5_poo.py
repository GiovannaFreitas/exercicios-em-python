'''Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, 
nome do correntista e saldo. Os métodos são os seguintes: 
alterarNome, depósito e saque; No construtor, saldo é opcional, 
com valor default zero e os demais atributos são obrigatórios.'''



class ContaCorrente:

    def __init__(self, conta="", correntista="", saldo=0):
        self.conta = conta
        self.correntista = correntista
        self.saldo = saldo

    
    def alterar_nome(self, nome):
        self.correntista.replace(nome)
        return self.correntista

    
    def fazer_deposito(self):

        return self.conta


    def fazer_saque(self):
        return self.saldo


correntista = input('Digite o nome do correntista: ')
conta = int(input("Digite o número da conta: "))
c = ContaCorrente(correntista)
cont = ContaCorrente(conta)
c.alterar_nome("")
cont.fazer_deposito()



