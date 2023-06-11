num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):

    # A cada dez números dá um quebra de linha
    if c % 10 == 0:
        print('\n')

    # Se o número for divisível por 1 ou ele mesmo colorir de azul e exibir
    if num % c == 0:
        print('\033[34m', end='')
        total += 1

    # Se não colorir de vermelho e exibir
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\n\033[mO número {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('\033[34mELE É UM NÚMERO PRIMO.')
else:
    print('\033[31mELE NÃO É UM NÚMERO PRIMO.')
