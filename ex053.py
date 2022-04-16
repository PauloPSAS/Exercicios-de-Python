frase = input('Digite algo: ').upper().replace(" ", "")
print('O inverso de {} é {}.'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('A frase digitada é um Palíndromo"')
else:
    print('A frase digitada não é um Palíndromo')
