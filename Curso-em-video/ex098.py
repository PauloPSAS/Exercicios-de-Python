from time import sleep

azul = '\033[36m'
amarelo = '\033[1;33m'
verde = '\033[32m'
vermelho = '\033[31m'


def contador(i, f, p):
    print(f'{azul}Contagem de {i} até {f} de {abs(p)} em {abs(p)}{amarelo}')
    if p > 0:
        for x in range(i, f + 1, p):
            print(x, end=' ')
            sleep(.3)
        print('FIM!')
    else:
        for x in range(i, f - 1, p):
            print(x, end=' ')
            sleep(.3)
        print('FIM!')


# main
print(f'{vermelho}-=' * 20)
contador(1, 10, 1)
print('FIM!\033[m')
print(f'{vermelho}-=' * 20)
contador(10, 0, - 2)
print(f'{vermelho}-=' * 20)
print(f'{azul}Agora é a sua vez de personalizar a contagem!{verde}')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
while True:
    if pas == 0:
        print('\nERRO! evite usar o valor 0 como passo. escolha outro número inteiro...')
        pas = int(input('Passo: '))
    else:
        break
print(f'{vermelho}-=' * 20)
contador(i=ini, f=fim, p=pas)
