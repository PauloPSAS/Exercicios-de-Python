import moeda

valor = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(valor)} é R$ {moeda.metade(valor, True)}')
print(f'O dobro de R$ {moeda.moeda(valor)} é R$ {moeda.dobro(valor, True)}')
print(f'Aumento de 10% de R$ {moeda.moeda(valor)} é {moeda.aumentar(valor, 10, True)}')
print(f'Reduzindo 13% temos R$ {moeda.diminuir(valor, 13, True)}')
