from random import randint
from time import sleep
tentativas = 1
print('\nO computador vai escolher um número entre 0 e 10 e você terá que adivinhar.\n')
print('Escolhendo...')
print('.')
sleep(0.5)
print('..')
sleep(0.5)
print('...')
sleep(0.5)
aleatorio = randint(0, 10)
print('PRONTO!\n')
print('Agora escolha um número de 0 a 10:', end=' ')
num = int(input())
while num != aleatorio:
    print('Você errou!')
    if num < 0 or num > 10:
        print('Por favor brinque sério escolha só entre 0 e 10')
        tentativas -= 1
    tentativas += 1
    num = int(input('Escolha novamente!: '))
print('Que bom você Conseguiu eu realmente escolhi o número {}.'.format(aleatorio))
print('Você conseguiu em {} tentativas.'.format(tentativas))
