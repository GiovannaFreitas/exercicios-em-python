'''Classe Funcionário: Implemente a classe Funcionário.
Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) 
e métodos para devolver nome e salário. Escreva um pequeno 
programa que teste sua classe.

Aprimore a classe do exercício anterior para adicionar o 
método aumentarSalario (porcentualDeAumento) que aumente o 
salário do funcionário em uma certa porcentagem.
Exemplo de uso:
  harry=funcionário("Harry",25000)
  harry.aumentarSalario(10)'''

class Funcionario():


    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


    def nome(self):
        return self.nome


    def salario(self):
        return self.salario


    def aumentar_salario(self, aumento):
        self.novo_salario += self.salario * aumento
        return f"Salário anterior: {self.salario}\nSalário com aumento: {self.novo_salario}" 


p1 = Funcionario("Giovanna", 1000)
p1.aumentar_salario(0.1)
