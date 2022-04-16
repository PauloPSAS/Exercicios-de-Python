num = (int(input('Digite um número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto valor: ')))
print(f'Os valore digitados foram: {num}')
print(f'O número 9 apareceu {num.count(9)} vez(s).')
if 3 in num:
    print(f'O número três apareceu na {num.index(3)}ª posição.')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
