from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa\n''')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        resultado = n1 + n2
        print('=-=' * 13)
        print('\033[34mA soma entre {} + {} = {}\033[m'.format(n1, n2, resultado))
        print('=-=' * 13)
    elif opcao == 2:
        resultado = n1 * n2
        print('=-=' * 13)
        print('\033[32mA multiplicação entre {} x {} = {}\033[m'.format(n1, n2, resultado))
        print('=-=' * 13)
    elif opcao == 3:
        if n1 > n2:
            resultado = n1
            print('=-=' * 13)
            print('\033[33mMaior entre {} e {} é: {}.\033[m'.format(n1, n2, resultado))
            print('=-=' * 10)
        elif n1 < n2:
            resultado = n2
            print('=-=' * 13)
            print('\033[33mMaior entre {} e {} é: {}.\033[m'.format(n1, n2, resultado))
            print('=-=' * 10)
        else:
            print('=-=' * 13)
            print('\033[33mAmbos são iguais\033[m')
            print('=-=' * 13)
    elif opcao == 4:
        print('\033[36mInforme os números novamente:\033[m')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\033[35mFinalizando...\033[m')
    else:
        print('\033[31mOPÇÃO INVALIDA, tente novamente.\033[m')
    sleep(1.5)

print('\033[35mFim do programa! Volte sempre')
