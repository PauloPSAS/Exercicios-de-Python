peso = float(input('Informe seu peso: (Kg) '))
altura = float(input('Informe sua altura: (m) '))
imc = peso / altura ** 2
print('Seu IMC é {:.1f}.'.format(imc), end=' ')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
else:
    print('OBESIDADE MÓRBIDA')
