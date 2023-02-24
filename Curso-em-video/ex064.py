qtd = n = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    qtd += 1
    soma += n
print('Você digitou {} números e a soma entre eles foi {}'. format(qtd - 1, soma - 999))
