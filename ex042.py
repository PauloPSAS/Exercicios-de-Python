print('-=' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO pois todos os lados são iguais')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é ESCALENO pois todos os lados são diferentes')
    else:
        print('O triângulo é ISÓSCELES pois tem dois lados iguais e um diferente')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
