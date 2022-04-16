km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias com o carro? '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}.'.format(total))
