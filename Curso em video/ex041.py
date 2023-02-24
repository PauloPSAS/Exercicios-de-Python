from datetime import date

ano = int(input('Em que ano o atleta nasceu? '))  # Ano de nascimento do atleta
atual = date.today().year  # Ano atual da competição
idade = atual - ano  # Idade do atleta

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JÚNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
