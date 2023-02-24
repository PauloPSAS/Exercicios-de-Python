from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 10)
if computador == 0: #Computador escolhe Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('EU VENCI!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador escolhe Papel
    if jogador == 0:
        print('EU VENCI!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #Computador escolhe Tesoura
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('EU VENCI!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
print('-=-' * 10)
print('Jogador escolheu {}'.format(itens[jogador]))
print('Computador escolheu {}'.format(itens[computador]))
