valor = int(input('Escolha de qual valor será a tabuada: '))
for tabuada in range(1, 11):
    print('{} X {} = {}'.format(valor, tabuada, valor * tabuada))
print('FIM')
