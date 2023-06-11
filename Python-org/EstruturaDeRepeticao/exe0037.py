"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia
seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero)
no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto,
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes."""


def gordo_magro(cl):
    g = m = codG = codM = 0
    for ind, cliente in enumerate(cl):
        if ind == 0:
            g = cliente[1][1]
            m = cliente[1][1]
            codG = cliente[0]
            codM = cliente[0]
        else:
            if cliente[1][1] > g:
                g = cliente[1][1]
                codG = cliente[0]
            if cliente[1][1] < m:
                m = cliente[1][1]
                codM = cliente[0]
    return g, m, codG, codM


def alto_baixo(cl):
    a = b = codA = codB = 0
    for ind, cliente in enumerate(cl):
        if ind == 0:
            a = cliente[1][0]
            b = cliente[1][0]
            codA = cliente[0]
            codB = cliente[0]
        else:
            if cliente[1][0] > a:
                a = cliente[1][0]
                codA = cliente[0]
            if cliente[1][0] < a:
                b = cliente[1][0]
                codB = cliente[0]
    return a, b, codA, codB


def add_alt_e_pes(c):
    alt = float(input(f"\nDigite a altura do cliente (Nº {c}): m "))
    kg = float(input(f"Digite o peso do cliente (Nº {c}): Kg "))
    return alt, kg


def erro_codigo():
    print("\nCódigo já ultilizado, por favor insira outro código.")


def cria_codigo():
    cod = int(input("\nDigite o código do cliente (0 para encerrar o programa): "))
    print()
    return cod


def exibe_tela_alt_bai(alt, bai, coa, cob):
    print("Cliente mais alto:")
    print(f"Altura: m {alt:.2f}")
    print(f"Código: Nº {coa}")
    print("\nCliente mais baixo:")
    print(f"Altura: m {bai:.2f}")
    print(f"Código: {cob}\n")


def exibe_tela_gor_mag(gor, mag, cog, com):
    print("Cliente mais gordo:")
    print(f"Peso: Kg {gor:.3f}")
    print(f"Código: Nº {cog}")
    print("\nCliente mais magro:")
    print(f"Peso: Kg {mag:.3f}")
    print(f"Código: {com}\n")


clientes = []
codUltilizados = set()

while True:
    codigo = cria_codigo()
    if codigo == 0:
        break
    if codigo in codUltilizados:
        erro_codigo()
    else:
        altura, peso = add_alt_e_pes(codigo)

        clientes.append([codigo, [altura, peso]])
        codUltilizados.add(codigo)
alto_baixo(clientes)

alto, baixo, codAlto, codBaixo = alto_baixo(clientes)
exibe_tela_alt_bai(alto, baixo, codAlto, codBaixo)

gordo, magro, codGordo, codMagro = gordo_magro(clientes)
exibe_tela_gor_mag(gordo, magro, codGordo, codMagro)
