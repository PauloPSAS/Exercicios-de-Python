# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def exibe_num(n):
    print("O número informado foi {}".format(n))


while True:
    numero = input("Digite um número: ")
    if numero.isnumeric():
        exibe_num(numero)
        break
    else:
        print("\033[31mDigite um número inteiro.\033[m\n")
