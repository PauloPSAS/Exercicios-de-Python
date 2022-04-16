num = int(input('Digite um número para o fatorial: '))
fator = num
total = 1
print('{}! = '.format(num), end='')
while fator > 0:
    print('{}'.format(fator), end='')
    print(' x ' if fator > 1 else ' = ', end='')
    total *= fator
    fator -= 1
print(total)
