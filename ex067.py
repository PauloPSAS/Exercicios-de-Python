while True:
    num = int(input('Digite um número para sua tabuada (Digite um número negativo para encerrar): '))
    print('__' * 10)
    cont = 1
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    print('__' * 10)
print('Fim do programa! Volte Sempre!')
