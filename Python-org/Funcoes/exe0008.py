# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def cont_num(value):
    def output(v, c):
        print(f'O número {v} tem {c} digito(s).')

    cont = 0
    for n in value:
        cont += 1
    output(value, cont)


while True:
    num = str(input("Digite um número inteiro: "))
    if num.isnumeric():
        break
    else:
        print("Apenas um número inteiro qualquer (Sem '.' ou ',' ou casas décimais).")
cont_num(num)
