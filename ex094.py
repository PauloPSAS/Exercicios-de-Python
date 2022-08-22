pessoa = dict()
grupo = list()
media_idade = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    media_idade += pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    while True:
        rsp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if rsp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if rsp == 'N':
        break
print()
print('==' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoa(s) cadastrada(s).')
print(f'B) A média de idade é de {media_idade / len(grupo):.1f} anos.')
print(f'C) A(s) Mulher(es) cadatrada(as) foram: ', end='')
x = 1
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'], end='')
        print(', ', end='' if x != len(grupo) else '. ')
    x += 1
print(f'\n D) Lista de pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] >= media_idade:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
