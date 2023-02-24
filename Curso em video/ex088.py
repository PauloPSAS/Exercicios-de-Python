from random import randint
from time import sleep

lista = []
num = cont = 0
print('=' * 40)
print('{:^40}'.format('PALPITES DA MEGA SENA'))
print('=' * 40)
print()
jogos = int(input('Quantos jogos você quer sortear? '))
print()
print('--' * 5, f' SORTEANDO {jogos} JOGOS ', '--' * 5)
sleep(1)
for j in range(0, jogos):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    cont = 0
    lista.sort()
    print(f'Jogo {j + 1}: {lista}')
    sleep(0.5)
    lista.clear()
print('==' * 5, ' < BOA SORTE! > ', '==' * 5)
