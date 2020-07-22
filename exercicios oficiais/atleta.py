"""Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04"""
atleta = input("Atleta: ").title()
notas = 0
for n in range(2):
    n = input("Nota: ")
    melhor_nota = max(n)
    pior_nota = min(n)
print("Resultado final: ")
print(f"Atleta: {atleta}")
print(f"Melhor nota: {melhor_nota:.1f}")
print(f"Pior nota: {pior_nota:.1f}")