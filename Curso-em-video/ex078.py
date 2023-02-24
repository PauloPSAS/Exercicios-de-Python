valores = list()
maior = menor = 0

for contador in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {contador}: ')))
    if contador == 0:
        maior = menor = valores[contador]
    else:
        if valores[contador] > maior:
            maior = valores[contador]
        if valores[contador] < menor:
            menor = valores[contador]
print('=-=' * 20)
print(f'\033[1;33mVocê digitou os valores: \033[1;35m{valores}\033[m')
print(f'\033[1;31mO maior valor digitado foi \033[1;35m{maior}\033[m \033[1;31mno(s) índice(s) ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'[{i}]... ', end='')
print(f'\n\033[1;34mO menor valor digitado foi \033[1;35m{menor}\033[m \033[1;34mno(s) índice(s) ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'[{i}]... ', end='')
