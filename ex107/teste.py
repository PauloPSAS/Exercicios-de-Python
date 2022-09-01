import moeda

valor = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {valor:.2f} é R$ {moeda.metade(valor):.2f}')
print(f'O dobro de R$ {valor:.2f} é R$ {moeda.dobro(valor):.2f}')
print(f'Aumento de 10% de R$ {valor:.2f} é {moeda.aumentar(valor, 10):.2f}')
