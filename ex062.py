print('Gerador de PA')
print('=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('...')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('\nProgressão finalizada com %d termos mostrados' % total)
