num = list()
resposta = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado...\n')
    else:
        print('Valor duplicado! não vou adicionar...\n')
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    while resposta not in 'SsNn':
        print('Digite Apenas [S/N]\n')
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resposta in 'Nn':
        break
print('=-=' * 15)
num.sort()
print(f'Você digitou: {num}')
