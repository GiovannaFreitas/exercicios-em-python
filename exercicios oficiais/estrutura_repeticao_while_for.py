#números entre 1 e 50 que são pares
# n = 1
# for n in range(1, 50):
#     if n % 2 == 0:
#         print(n)
# contador = 0
# numero = -1
# while numero < 1 or numero > 10:
#     numero = int(input('Digite um número válido: '))
# print(f'Tabuada de {numero}: ')
# if numero >= 1 and numero <= 10:
#     while contador != 10:
#         contador += 1
#         print(f'{numero} x {contador} =',numero * contador)
# else:
#     print('Número inválido')
#Faça um programa que peça um número inteiro e determine se ele
# é ou não um número primo.
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.
#print(f'{numero} é primo')numero = int(input('digite um número para saber se é primo: '))
#while:
#numero impar entre 1 e 50
#for numero in range(1, 51, 2):
    #print(numero)
# numero_escolhido = 47
# numero = 99999
# while numero != numero_escolhido:
#     numero = int(input('Digite outro número: '))
#     if numero < 47:
#         print('É maior que esse')
#     elif numero > 47:
#         print('É menor que esse')
#     else:
#         print('Esse foi o número escolhido')
# n = int(input('Digite a quantidade de pessoas: '))
# soma = 0
# for x in range (n):
#     idade = int(input('Digite sua idade: '))
#     while idade <= 0:
#         print('Idade inválida')
#         idade = int(input('Digite a idade: '))
#     soma += idade #soma = soma + idade
# media = soma/n
# if media >= 0 and media <= 25:
#     perfil = 'Jovem'
# elif media >= 26 and media <= 60:
#     perfil = 'Adulta'
# elif media > 60: #não foi usado else porque pode ser que digite uma idade negaiva sem querer
#     perfil = 'Idosa'
# print(f'A média de idade é {media} e a turma é {perfil}')
# nome = input('Nome do usuário: ').lower()
# senha = input('Senha: ').lower()
# while nome == senha:
#       print('Digite um nome de usuário diferente da senha: ')
#       nome = input('Nome do usuário: ').lower()
#       senha = input('Senha: ').lower()#pra diferenciar maiusculas e minusculas
#  else:
#      while not senha.isnumeric():
#          print('Senha deve conter somente número')
#          nome = input('Nome: ')
#          senha = input('Senha: ')
#      else:
#          print('Cadastro efetuado')
# nome = input('Nome: ')
#  while len(nome) < 3:
#      nome = input('Digite um número maior que 3 caracteres: ')
#  idade = input('Idade: ')
#  while idade < 0 or idade > 150:
#      idade = input('Digite uma idade entre 0 e 150: ')
#  salario = input('Digite seu salário: ')
#  while salario < 0:
#      salario = input('Digite um salário maior que 0: ')
# base = int(input('Digite a base: '))
# expoente = int(input('Digite o expoente '))
# potencia = 1
# for x in range(expoente):
#     potencia = potencia * base
# print(potencia)