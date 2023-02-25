"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve
converter 14:25 em 2:25 P.M. À entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um “loop” que
permita que o usuário repita esse cálculo para novos valores de entrada todas às vezes que desejar."""


def entrada():
    while True:
        h = int(input("Digite a hora (entre 0 e 23): "))
        if 0 <= h < 24:
            break
        else:
            print('Digite apenas entre 0 e 23 horas.\n')
    while True:
        m = int(input('Digite os minutos (entre 0 e 59): '))
        if 0 <= m < 60:
            break
        else:
            print("Digite apenas entre 0 e 59 minutos.\n")

    return h, m


def conversao(ho):
    if ho >= 12:
        if ho == 12:
            padrao = 'P.M'
            return ho, padrao
        ho -= 12
        padrao = 'P.M'
        return ho, padrao
    else:
        if ho == 0:
            ho = 12
        padrao = 'A.M'
        return ho, padrao


def saida(hour, minute):
    hour, pattern = conversao(hour)
    print(f'em formato de 12 horas são: {hour}:{minute} {pattern}.')


while True:
    hours, minutes = entrada()
    print()
    saida(hours, minutes)
    while True:
        response = str(input("\nQuer continuar [S/N]? ")).upper()
        if response == 'S' or response == 'N':
            break
        else:
            print("Digite apenas 'S' para Sim ou 'N' para Não.")
    if response == 'N':
        break
