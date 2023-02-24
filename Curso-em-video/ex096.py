def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f} x {c:.1f} é de {a:.1f}m².')


# main
print('=' * 20)
print('controle de terrenos')
print('=' * 20)
area(
    float(input('LARGURA (m): ')),
    float(input('COMPRIMENTO (m): '))
)
