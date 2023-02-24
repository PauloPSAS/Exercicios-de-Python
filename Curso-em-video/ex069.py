maior18 = homens = mulheres = 0
while True:
    print('---' * 15)
    print('CADASTRE UMA PESSOA')
    print('---' * 15)
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo == 'M':
        homens += 1
    if sexo == 'M' and idade < 20:
        mulheres += 1
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continua != 'S' and continua != 'N':
        print('Digite apenas "S" para Sim ou "N" para Não')
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continua == 'N':
        break
    continua = ''
print('---' * 15)
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homem(s) cadastrado(s)')
print(f'E temos {mulheres} mulher(es) com menos de 20 anos')
