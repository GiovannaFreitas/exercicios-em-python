# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
# (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas
# no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a
# quantidade de hora é 220.
hours_for_months = float(input('Hours for months: '))
value_for_hour = float(input('Value for hour: '))
salary = (hours_for_months * value_for_hour)
print(f'Gross Salary: R$ {salary:.2f}')
if salary <= 900:
    ir = 'Isento'
    print('(-) IR: Free')
elif salary > 900 and salary <=1500:
    ir = (5/100) * salary
    print(f'(-) IR: R$ {ir} (5%)')
elif salary > 1500 and salary <= 2500:
    ir = (10/100) * salary
    print(f'(-) IR: R$ {ir} (10%)')
else:
    ir = (20/100) * salary
    print(f'(-) IR: R$ {ir} (20%)')
syndicate = (3/100) * salary
fgts = (11/100) * salary # responsible for the company
discount = ir + syndicate
fluid_salary = salary - discount
print(f'(-) Syndicate: R$ {syndicate} (3%)')
print(f'FGTS: R$ {fgts} (11%) for the company')
print(f'Total Discounts: R$ {discount:.2f}')
print(f'Fluid Salary: R$ {fluid_salary:.2f}')