"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 8.00
    Dinheiro: R$ 20.00
    Troco: R$ 12.00
    ..."""

from time import sleep


def comprovante(pr, to, tr, d):
    print("\nComprovante das Lojas Tabajara.")
    for p in range(1, len(pr)+1):
        print(f"Produto {p}: R$ {pr[p-1]:.2f}")
    print(f"Valor Total: R$ {to:.2f}")
    print(f"Dinheiro Pago: R$ {d:.2f}")
    print(f"Troco: R$ {tr:.2f}")
    print("Obrigado e Volte Sempre!")


def dinheiro_troco(t):
    print("Total: R$ {:.2f}".format(t))
    while True:
        d = float(input("Dinheiro: R$ "))
        if d < t:
            print("O dinheiro pago têm que ser maior que o valor total.")
        else:
            print("Troco: R$ {:.2f}".format(d - t))
            break
    tr = d - t
    return tr, d


def valor_produtos():
    import sys

    t = 0
    c = 0
    produtos = []
    while True:
        c += 1
        produtos.append(float(input(f"Produto {c}: R$ ")))
        if c == 1 and produtos[c-1] == 0:
            print("\nVocê não comprou nada...")
            print("Até a próxima")
            sys.exit()

        if produtos[c - 1] == 0:
            produtos.pop()
            c -= 1
            break
        t += produtos[c - 1]

    return t, produtos


print("Lojas Tabajara")
total, produts = valor_produtos()
troco, dinheiro = dinheiro_troco(total)

sleep(3)
comprovante(produts, total, troco, dinheiro)
