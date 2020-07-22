class Tamagotchi:
    bichinho_feliz = """:)"""


    def __init__(self, nome="Tamagotchi", bucho=[]):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        return self.bichinho_feliz

    def ver_bucho(self):
        return f"bucho de {self.nome}: {self.bucho}"


    def digerir(self):
        self.bucho.clear()
        return "bucho limpo"

nome = input('Digite o nome do seu tamagotchi: ')
comida1 = input("Digite a comida 1")
t1 = Tamagotchi("Lindinha")
t2 = Tamagotchi(nome)
t1.comer("Torta de Cogumelos")
print(t1.ver_bucho())
t1.comer("Brigadeirão")
print(t1.ver_bucho())
t2.comer(comida1)
t1.comer(t2)
    

