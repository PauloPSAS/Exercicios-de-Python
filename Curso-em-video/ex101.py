def idade(a):
    import datetime
    ano_atual = datetime.date.today().year
    return ano_atual - a


def voto(anos):
    if anos < 16:
        return 'NÃO VOTA'
    elif 18 <= anos < 64:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'


# Main
print("==" * 20)
ano = int(input("Em que ano você nasceu? "))
i = idade(ano)
x = voto(i)
print(f"Com {i} anos: {x}.")
print("==" * 20)
