def fatorial(n, show=False):
    """
    → Calcula o valor fatorial de um número.
    :param n: É o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: retorna o valor fatorial de n.
    """
    if not show:
        from math import factorial
        return factorial(n)
    else:
        f = 1
        for v in range(n, 0, -1):
            print(v, end='')
            print(' x ' if v > 1 else ' = ', end='')
            f *= v
        return f


# Programa principal
fact = int(input('Digite um valor para mostrar seu Fatorial: '))
while True:
    resp = str(input('Quer mostrar o calculo [S/N]? ')).strip().upper()[0]
    if resp in 'SN':
        break
    else:
        print('ERRO! Por favor, digite apenas S ou N...')
print('==' * 25)
if resp == 'S':
    print(fatorial(fact, True))
else:
    print(f'O fatorial de {fact} é: ', end='')
    print(fatorial(fact))
print('==' * 25)
