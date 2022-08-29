def leiaInt(msg):
    num = input(f'{msg}')
    if num.isnumeric():
        return int(num)
    else:
        while True:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            num = input(f'{msg}')
            if num.isnumeric():
                break
        return int(num)


# Main
n = leiaInt('Digite um número: ')
print(f'\033[36mVocê acabou de digitar o número {n}.\033[m')
