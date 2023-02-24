num = int(input('Digite um número para conversão: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
x = int(input('Sua opção: '))

# [2:] irá remover os caracteres de especificação
if x == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif x == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif x == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Escolha inválida. Digite 1, 2 ou 3 para conversão. Tente novamente.')
