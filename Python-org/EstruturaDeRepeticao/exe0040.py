"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:"""
# a) Código da cidade;
# b) Número de veículos de passeio (em 1999);
# c) Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e) Qual a média de veículos nas cinco cidades juntas;
# f) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

def input_citys():
    qdt = int(input("Quantas cidades serão analisadas? "))
    cidades = {}

    for city in range(1, qdt + 1):
        print()
        codigoCity = input("Digite o código (ou nome) da cidade: ")
        cidades[codigoCity] = {}
        cidades[codigoCity]['numero_veiculos'] = int(input('Digite o número de veiculos de passeio (em 1999): '))
        cidades[codigoCity]['acidentes'] = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))
        print()
    return cidades



def menor_indice_acidentes(c):
    index = 1
    menor = maior = 0
    cidadeMenInd = cidadeMaiInd = ''
    for cidade in c:
        if index == 1:
            menor = c[cidade]['acidentes']
            cidadeMenInd = cidade
            maior = c[cidade]['acidentes']
            cidadeMaiInd = cidade
        else:
            if c[cidade]['acidentes'] < menor:
                menor = c[cidade]['acidentes']
                cidadeMenInd = cidade
            if c[cidade]['acidentes'] > maior:
                maior = c[cidade]['acidentes']
                cidadeMaiInd = cidade
        index += 1
    return maior, cidadeMaiInd, menor, cidadeMenInd



def media_veiculos(c):
    media = 1
    for cidade in c:
        media += c[cidade]['numero_veiculos']
    media /= len(c)
    return media


def media_acidentes_menos2000(c):
    media = 1
    cont = 0
    for cidade in c:
        if c[cidade]['acidentes'] < 2000:
            media += c[cidade]['acidentes']
            cont += 1
    media /= cont
    return media
    

listaCidades = input_citys()
maiorIndAcidentes, cidadeMaiI, menorIndAcidentes, cidadeMenI = menor_indice_acidentes(listaCidades)

print(f"\nO maior índice de acidentes é de {maiorIndAcidentes}. Da cidade {cidadeMaiI}.")
print(f"O menor índice de acidentes é de {menorIndAcidentes}. Da cidade {cidadeMenI}.")

mediaVeiculos = media_veiculos(listaCidades)
print(f"\nA média de veiculos das {len(listaCidades)} cidades é de {mediaVeiculos:.1f} por cidade.")

mediaAcidentes = media_acidentes_menos2000(listaCidades)
if mediaAcidentes == 0:
    print("Não há cidades com menos de 2000 acidentes para se calcular a média.")
else:
    print(f"A média de acidentes nas cidades com menos de 2000 acidentes é de: {mediaAcidentes:.1f} acidentes por cidade.")
