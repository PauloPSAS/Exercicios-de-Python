"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
que é, a quantia de imposto sobre vendas expressas em porcentagem e custo, que é, o custo de um item antes do imposto. A
função “altera” o valor de custo para incluir o imposto sobre vendas."""


def soma_imposto(taxa_imposto, custo):
    percentual = taxa_imposto / 100 * custo
    t = percentual + custo
    return t


b = float(input('Digite o valor do produto: R$ '))
a = int(input('Quantos % é o imposto do produto (Um valor inteiro)? '))
total = soma_imposto(a, b)
print(f"O valor final do produto com {a}% de taxa é R$ {total:.2f}")
