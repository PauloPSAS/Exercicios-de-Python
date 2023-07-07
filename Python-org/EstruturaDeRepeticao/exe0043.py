# O cardápio de uma lanchonete é o seguinte:
"""Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado."""

produtos = {
    100: ('Cachorro Quente', 1.20),
    101: ('Bauru Simples', 1.3),
    102: ('Bauru com Ovo', 1.50),
    103: ('Hambúrguer', 1.20),
    104: ('Cheeseburguer', 1.30),
    105: ('Refrigerante', 1.00)
}

itens_comprados = []

print("----- Cardápio -----")
print("Código  Produto            Preço")
for codigo, produto in produtos.items():
    nome_produto = produto[0]
    preco_unitario = produto[1]
    print(f"{codigo: <7} {nome_produto: <20} R$ {preco_unitario:.2f}")
print("--------------------")

while True:
    codigo = int(input("\nDigite o código do item de acordo com o produto que você desejar: "))

    if codigo not in produtos:
        print("Digite apenas um código válido...")
        continue

    qtd = int(input("Digite a quantidade do item especificado: "))

    produto = produtos[codigo]
    nome_produto = produto[0]
    preco_unitario = produto[1]

    total_item = preco_unitario * qtd
    itens_comprados.append((nome_produto, qtd, total_item))

    while True:
        ctn = input("\nQuer continuar comprando? [S/N] ").upper()

        if ctn == 'S':
            break
        elif ctn == 'N':
            break
        else:
            print("Digite apenas S ou N...")

    if ctn == 'N':
        break

total_compra = sum(item[2] for item in itens_comprados)

print("\nProdutos comprados:")
for item in itens_comprados:
    nome_produto, qtd, total_item = item
    print(f"Produto: {nome_produto} | Quantidade: {qtd} | Total: R$ {total_item:.2f}")

print(f"\nTotal a pagar: R$ {total_compra:.2f}")
