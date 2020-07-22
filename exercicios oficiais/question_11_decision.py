# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite o valor do salário: '))
print(f'Salário: {salario}')
if salario <= 280:
    salario_atual = (salario * 1.20)
    print(f'Aumento: 20%\nValor do Aumento: {salario_atual - salario:.2f}\nSalário atual: {salario * 1.20:.2f}')
elif salario > 280 and salario < 700:
    salario_atual = (salario * 1.15)
    print(f'Aumento: 15%\nValor do Aumento: {salario_atual - salario:.2f}\nSalário atual: {salario * 1.15:.2f}')
elif salario > 700 and salario < 1500:
    salario_atual = (salario * 1.10)
    print(f'Aumento: 10%\nValor do Aumento: {salario_atual - salario:.2f}\nSalário atual: {salario * 1.10:.2f}')
elif salario >= 1500:
    print(f'Aumento: 5%\nValor do Aumento: {salario_atual - salario:.2f}\nSalário atual: {salario * 1.05:.2f}')



