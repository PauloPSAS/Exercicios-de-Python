import moeda

valor = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moeda.moeda(valor)} é R$ {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de R$ {moeda.moeda(valor)} é R$ {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumento de 10% de R$ {moeda.moeda(valor)} é {moeda.moeda(moeda.aumentar(valor, 10))}')
