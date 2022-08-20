from datetime import date

pessoa = dict()
ano_atual = date.today().year

pessoa["nome"] = str(input('Nome: ')).strip().title()
ano_nascimento = int(input('Ano de nascimento: '))
pessoa["idade"] = ano_atual - ano_nascimento
pessoa["ctps"] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa["ctps"] != 0:
    pessoa["contratação"] = int(input('Ano de contratação: '))
    pessoa["salário"] = float(input('Salário R$: '))
    pessoa["aposentadoria"] = (pessoa["contratação"] - ano_nascimento) + 35
print('-=' * 30)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor: {v}')
