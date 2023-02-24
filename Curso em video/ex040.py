n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('-==-' * 10)
print('Tirando {:.1f} e {:.1f}'.format(n1, n2))
print('A Media Final é {:.1f}'.format(media))
if media >= 7:
    print('APROVADO!')
elif 6.9 > media > 5:
    print('RECUPERAÇÃO')
    print('Precisa de {:.1f} na FINAL!'.format(7 - media))
else:
    print('REPROVADO!')
print('-==-' * 10)
