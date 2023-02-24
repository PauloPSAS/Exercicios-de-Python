from datetime import date
data = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    if data - ano >= 18:
        maior += 1
    else:
        menor += 1
print('\033[31mAo todo tivemos {} pessoas maiores de idade.'.format(maior))
print('\033[33mE também tivemos {} pessoas menores de idade.'.format(menor))
