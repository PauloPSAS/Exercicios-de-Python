from random import randint
print('\033[1;34mVAMOS JOGAR O JOGO DO \033[3mPAR\033[m \033[1;34mOU \033[3mÍMPAR!\033[m')
print('=-=' * 15)
cont = 0
while True:
    num = int(input('\nDiga um valor: '))
    lista = ' '
    while lista != 'p' and lista != 'i':
        lista = str(input('Par ou Ímpar? [P/I] ')).lower().strip()
    print('___' * 15)
    pc = randint(0, 10)
    total = num + pc
    print(f'\033[36mVocê jogou {num} e o computador {pc}.\nTotal é {total}\033[m')
    if total % 2 == 0:
        print('\033[33mDEU PAR\033[m')
        print('___' * 15)
        if lista == 'p':
            print('\033[34mVocê GANHOU!')
            print('Vamos jogar novamente...\033[m')
            cont += 1
        elif lista == 'i':
            print('\033[31mVocê PERDEU!\033[m')
            break
    else:
        print('\033[33mDEU ÍMPAR\033[m')
        print('___' * 15)
        if lista == 'p':
            print('\033[31mVocê PERDEU!\033[m')
            break
        elif lista == 'i':
            print('\033[34mVocê GANHOU!')
            print('Vamos jogar novamente...\033[m')
            cont += 1

print('=-=' * 15)
print(f'\033[1;33mGAME OVER! Você venceu {cont} vez(es) seguida(s).')
