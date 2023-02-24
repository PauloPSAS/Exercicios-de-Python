from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
alistamento = 18
idade = atual - nascimento
print('Quem nasceu em {} tem {} em 2022'.format(nascimento, idade))
if idade > alistamento:
    print('Você já deveria ter se alistado há {} anos'.format(idade - alistamento))
    print('Seu alistamento foi em {}'.format(atual - (idade - alistamento)))
elif idade < alistamento:
    print('Ainda faltam {} anos para o alistamento'.format(alistamento - idade))
    print('Seu alistamento será em {}'.format(atual + (alistamento - idade)))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
