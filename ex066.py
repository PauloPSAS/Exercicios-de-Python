c = n = s = 0
while True:
    n = int(input('\033[31mDigite um valor inteiro [999 para encerrar o programa]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'\033[33mVocê digitou {c} número(s) e soma entre ele(s) é {s}')
