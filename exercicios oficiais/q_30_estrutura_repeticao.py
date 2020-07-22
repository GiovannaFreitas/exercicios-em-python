price = float(input('Digite o preço do pão R$: '))
print('Panificadora Pão de Ontem - Tabela de Preços')
for x in range(1, 52):
    quantity = x
    print(f'{quantity} - R$ {quantity * price:.2f}')
    
    
    
