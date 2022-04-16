x = str(input('Digite seu nome completo: ')).strip().split()
print('\nPrazer em te Conhecer!\n')
print('Seu Primeiro nome é {}.'.format(x[0]))
print('Seu Último nome é {}.'.format(x[-1]))

"""
Ultimo nome também pode ser feito da seguinte forma
print('Seu último nome é {}'.format(x[len(nome) -1]))
"""
