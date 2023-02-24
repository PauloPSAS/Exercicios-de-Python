def metade(v=0, form=False):
    """
    → Mostra a metade de um determinado valor.
    :param v: valor que será dividido pela metade.
    :param form: Forma com a qual será exibido o valor.
    :return: O resultado do valor e a forma com a qual será mostrada
    """
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


def moeda(v: object = 0, m='R$ '):
    return f'{m}{v:.2f}'.replace('.', ',')
