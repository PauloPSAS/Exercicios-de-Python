from random import randint
from time import sleep
print('-=-' * 27)
print('Vou escolher um número entre 0 e 5, você deve adivinhar que número escolhi ok?')
print('-=-' * 27)
print('\n')
print('-=-' * 27)
rand = randint(0, 5)
n = int(input('\nQue número escolhi? '))
print('PROCESSANDO...\n')
sleep(1.2)
if rand == n:
    print('Parabéns, Você acertou!')
    print('Eu realmente escolhi o número {}!'.format(rand))
else:
    print('Você errou...')
    print('Eu escolhi o número {}.,\n'.format(rand))
    print('Não desanime, tente novamente')
print('-=-' * 27)