print('LOJAS TABAJARA')#Digite 0 para concluir a compra
quantity = 1
total = 0
price = float(input('Price R$ '))
print(f'Product {quantity}: R$ {price:.2f}')
while price > 0:
     quantity += 1
     total = total + price
     price = float(input('Price R$ '))
     print(f'Product {quantity}: R$ {price:.2f}')
     if price == 0:
         money = float(input('Money: R$ '))
         rest = (money - total)
         print(f'TOTAL R$ {total:.2f}\nMONEY R$ {money:.2f}\nREST R$ {rest:.2f}')
#sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
# # while sexo not in 'MmFf':
#     sexo = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
# print(f'sexo {sexo} registrado com sucesso')