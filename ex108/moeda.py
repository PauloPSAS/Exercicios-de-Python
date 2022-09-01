def metade(v=0):
    res = v / 2
    return res


def dobro(v=0):
    res = v * 2
    return res


def aumentar(v=0, t=0):
    res = v + (v * t / 100)
    return res


def diminuir(v=0, t=0):
    res = v - (v * t / 100)
    return res


def moeda(v=0, m='R$ '):
    return f'{m}{v:.2f}'.replace('.', ',')
