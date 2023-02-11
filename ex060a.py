num = int(input('Digite um número: '))
fator = num
total = 1
print('{}! = '.format(num), end='')
for fator in range(num, 0, -1):
    print('{}'.format(fator), end='')
    print(' x ' if fator > 1 else ' = ', end='')
    total *= fator
print(total)
