num = contador = 0
maior = menor = 0
media = antes = m_final = 0
texto = ' '
while texto != 'n':
    num = int(input('Digite um número: '))
    texto = str(input('Quer continuar? [S/N]: ')).strip().lower()
    contador += 1
    antes = num
    media += antes
    if contador == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    while texto != 's' and texto != 'n':
        print('Digite apenas [S/N] para SIM ou NÃO')
        texto = str(input('Quer continuar? [S/N]: ')).strip().lower()
print('\n')
m_final = media / contador
print('Você digitou {} número(s) e a média foi {:.1f}'.format(contador, m_final))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
