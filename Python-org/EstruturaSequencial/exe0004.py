# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def msg_erro():
    print("Digite uma nota apenas entre 0 e 10")


total = 0
for value in range(1, 5):
    while True:
        n = float(input(f"Qual a {value}º nota: "))
        if 0 > n > 10:
            msg_erro()
        else:
            break
    total += n
total /= 4
print("A média é {:.1f}".format(total))
