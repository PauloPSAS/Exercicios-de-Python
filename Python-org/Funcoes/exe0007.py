"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma
conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes
valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a
chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir
outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste
momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de
prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso."""


def valor_pagamento(prt, dias_a):
    juros = 0
    if dias_a > 0:
        juros = prt / 100 * 3
        for d in range(dias_a):
            juros += prt / 100 * 0.1
    return juros


totalPrestacoes = qtd = 0
while True:
    prestacao = float(input("diga o valor da prestação: R$ "))
    if prestacao == 0:
        break
    diasAtraso = int(input("Digite os dias de atraso: "))
    total = valor_pagamento(prestacao, diasAtraso) + prestacao
    totalPrestacoes += total
    qtd += 1
    print(f'Total a ser pago com {diasAtraso} dias de atraso é R$ \033[1;31m{total:.2f}\033[m')
print("")
print(f"\033[1;35m{' < RELATÓRIO TOTAL > ':^40}\033[m")
print(f"\033[33mTotal de prestações pagas: {qtd}")
print(f"\033[34mTotal de todas prestações pagas é: R$ {totalPrestacoes:.2f}\033[m")
print('__' * 40)
