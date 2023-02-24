soma_idade = 0
media_idade = 0
maior_idade = 0
mulheres = 0
pessoa_velha = ''
for p in range(1, 5):
    print('_____%dª PESSOA _____' % p)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    soma_idade += idade
    if sexo == 'f' and idade < 20:
        mulheres += 1
    if p == 1 and sexo == 'm':
        maior_idade = idade
        pessoa_velha = nome
    else:
        if idade > maior_idade:
            maior_idade = idade
            pessoa_velha = nome
media_idade = soma_idade / 4
print('A media de idade do grupo é de %.1f anos.' % media_idade)
print('O homem mais velho do grupo se chama {} e tem {} anos.'.format(pessoa_velha, maior_idade))
print('No grupo tem %d mulher(es) com menos de 20 anos.' % mulheres)
