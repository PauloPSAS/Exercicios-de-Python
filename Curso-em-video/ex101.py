def idade(n):
    from datetime import datetime
    ano_atual = datetime.today().year
    idd = ano_atual - n
    return idd


def voto(a):
    if a <= 15:
        print('\033[1;31mNÃO VOTA.')
    elif a <= 17 or a > 65:
        print('\033[1;36mVOTO OPCIONAL.')
    else:
        print('\033[1;34mVOTO OBRIGATÓRIO.')


i = idade(int(input('Em que ano você nasceu? ')))
print(f'Com {i} anos: ', end='')
voto(i)
