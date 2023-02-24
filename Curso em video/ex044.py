produto = float(input('Qual é o valor da compra: R$ '))
print('-=-' * 20)
print('''
 Digite [ 1 ] para à vista dinheiro/Cheque: 10% Desconto.
 Digite [ 2 ] para à vista no cartão: 5% Desconto.
 Digite [ 3 ] para 2x no cartão: Preço normal.
 digite [ 4 ] para 3x ou mais no cartão: 20% juros.\n''')
print('Escolha a forma de pagamento: ', end=' ')
forma = int(input())
print('-=-' * 20)
if forma == 1:
    produto = produto - (produto * 10 / 100)
    print('Total a pagar: R${:.2f}'.format(produto))
elif forma == 2:
    produto = produto - (produto * 5 / 100)
    print('Total a pagar: R${:.2f}'.format(produto))
elif forma == 3:
    print('Parcelado em 2x de R${:.2f} SEM JUROS'.format(produto / 2))
    print('Total a pagar: R${:.2f}'.format(produto))
elif forma == 4:
    produto = produto + (produto * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print('Parcelado em {}x de R${:.2f} COM 20% DE JUROS'.format(parcelas, produto / parcelas))
    print('Total a pagar: R${:.2f}'.format(produto))
else:
    print('Forma de pagamento Inválida.')
