sexo = input('Qual o seu Sexo? [M/F]: ').upper().strip()
while sexo != 'M' and sexo != 'F':
    print('Por favor digite apenas "M" ou "m" para Homem e "F" ou "f" para mulher.')
    sexo = input('Qual o seu Sexo? [M/F]: ').upper().strip()
if sexo == 'M':
    print('MASCULINO!')
elif sexo == 'F':
    print('FEMININO!')
