""" Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma ‘string’ no
formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida."""


def dma():
    while True:
        dia = input('Digite o dia: ')
        if dia.isnumeric() and 31 >= int(dia) >= 1:
            break
        else:
            print('Digite apena o dia entre 1 e 31. (Sem letras ou sinais).\n')
    while True:
        mes = input('Digite o mês: ')
        if mes.isnumeric() and 12 >= int(mes) >= 1:
            break
        else:
            print('Digite apena o mês entre 1 e 12. (Sem letras ou sinais).\n')
    while True:
        ano = input('Digite o ano que você deseja, apenas os 4 digitos: ')
        if ano.isnumeric() and 3500 >= int(ano) >= 1000:
            break
        else:
            print('Tente digitar um ano lógico menor que 3500 ou maior do que 1000 e sem sinais ou letras...\n')
    return dia, mes, ano


def output(dia, mes, ano):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']

    print(f'\n\033[1;33mDia {int(dia)} de {meses[int(mes)-1]} de {int(ano)}.')


d, m, a = dma()
output(d, m, a)
