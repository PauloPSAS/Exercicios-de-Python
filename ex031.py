print('\nViagens abaixo de 200Km de distância tem o valor de R$0.50 por Km')
print('Viagens acima de 200Km de distância tem o valor de R$0.45 por Km\n')
x = float(input('De quantos Km foi a Viagem? '))
if x <= 200:
    y = x * 0.50
else:
    y = x * 0.45
print('O valor da passagem é  de R${:.2f}.'.format(y))
