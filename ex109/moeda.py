def metade(v=0, form=False):
    res = v / 2
    return res if not form else moeda(res)


def dobro(v=0, form=False):
    res = v * 2
    return res if not form else moeda(res)


def aumentar(v=0, t=0, form=False):
    res = v + (v * t / 100)
    return res if form is False else moeda(res)


def diminuir(v=0, t=0, form=False):
    res = v - (v * t / 100)
    return res if form is False else moeda(res)


def moeda(v=0, m='R$ '):
    return f'{m}{v:.2f}'.replace('.', ',')
