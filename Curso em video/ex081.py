valores = []
while True:
    valores.append(int(input('\nDigite um valor: ')))
    resp = str(input('Quer continuar? ')).upper().strip()
    while resp not in 'SsNn':
        print('Digite apenas ["S" para SIM / "N" para NÃO]\n')
        resp = str(input('Quer continuar? ')).upper().strip()
    if resp in 'Nn':
        break
print('=-=' * 15)
print(f'Você digitou {len(valores)} elemento(s).')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista')
