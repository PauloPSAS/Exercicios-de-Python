from random import randint
n = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), 
print('\033[1;31mOs valores sorteados foram: ', end='')
for num in n:
    print(f'\033[3;35m{num}', end=' ')
print(f'\n\n\033[1;33mO maior valor sorteado foi: \033[3;35m{max(n)}')
print(f'\033[1;34mO menor valor sorteado foi: \033[3;35m{min(n)}')
