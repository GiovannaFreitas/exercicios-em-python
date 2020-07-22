from random import choice
nomes = ['João', 'Maria', 'Giovanna', 'Vitor', 'Ricardo', 'Hugo', 'Rhayra', 'Thiago', 'Luana', 'Anderson', 'Mateus', 'Isabel', 'Isa', 'Nay', 'Deize', 'Julio', 'Raul', 'Joana', 'Thaynan', 'Marcela']
sobrenomes = ['Freitas', 'Rodrigues', 'Silva', 'Soares', 'Almeida', 'Gomes', 'Carvalho', 'Nascimento', 'Pereira', 'Coutinho', 'Barros', 'Ferreira', 'Braga', 'Teixeira', 'Andrade', 'Lispector', 'Oliveira', 'Trindade', 'Costa', 'Martins']
idade = [20, 22, 16, 18, 19, 23, 38, 40, 25, 34, 32, 33, 26, 24, 22, 21, 29, 10, 15, 27]
num = int(input('Digite um número de 1 a 20:  '))

if 1 > num > 20:
    num = int(input('Digite um número de 1 a 20: '))

else:
    arquivo = open('lista.txt', 'w')
    for n in range(num):
        arquivo.writelines(choice(nomes))
arquivo.close()

