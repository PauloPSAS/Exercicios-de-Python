"""Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor
entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
primeira jogada, isto é chamado "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde,
no entanto, se tirar um 7 antes de tirar este Ponto novamente."""

import time
import sys


def rola_dados():
    import random

    _ = input('Pressione ENTER para rolar os dados.')

    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    s = d1 + d2
    print(f'A soma dos dados rolando foi {d1} + {d2} = {s}')
    time.sleep(.5)
    return s


def wlc(sdados):
    print(f'Você tirou {sdados}.\n')
    time.sleep(1)
    if cont == 1:
        if sdados == 7 or sdados == 11:
            print('QUE SORTE!!!')
            time.sleep(1)
            print('Você é um "Natural" ganhou de primeira, PARABÉNS!')
            sys.exit()
        elif sdados == 2 or sdados == 3 or sdados == 12:
            print("Que azar...")
            time.sleep(1)
            print('Logo "Craps" de primeira... Quem sabe na próxima.')
            sys.exit()
        else:
            pontos = sdados
            print(f'Então {pontos} é seus pontos tente tirar ele novamente antes de tirar um 7.')
            time.sleep(1)
            return pontos


while True:
    start = input('Vamos começar? digite [S/N]: ').upper()
    if start == 'N':
        print('\nJogaremos numa próxima oportunidade então. Tchau!')
        sys.exit()
    elif start == 'S':
        break
    else:
        print("Digite apenas 'S' ou 'N'.\n")

cont = 1
time.sleep(.5)
print(f'{"BEM VINDO AO JOGO!":^40}')
print(f"{'VAMOS TESTAR SUA SORTE ENTÃO.':^40}")
time.sleep(1)
somaDados = rola_dados()
p = wlc(somaDados)

while True:
    cont += 1
    somaDados = rola_dados()
    if somaDados == 7:
        time.sleep(1)
        print("Você perdeu... Tente novamente na próxima.")
        print(f'Você rolou os dados {cont} vezes.')
        break
    elif somaDados == p:
        time.sleep(1)
        print('PARABÉNS!!! Você ganhou!!!')
        print(f'Você rolou o dado {cont} vezes')
        break
    else:
        print('Jogue os dados novamente.\n')
        time.sleep(1.5)
print('FIM')
