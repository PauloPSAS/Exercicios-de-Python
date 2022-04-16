lista = [[], []]
x = 0

for c in range(1, 8):
    x = int(input(f'Digite o {c}º valor: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

print('=-=' * 20)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
