#question 4 (consertar erros)
vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
letra = input("Digite uma letra: ")
if letra in vogais:
     print("é uma vogal")
elif letra.isalpha():
    print("é uma consoante")
else:
    print("não é uma vogal ou consoante")
print('fim')
input()
