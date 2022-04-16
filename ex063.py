print('\033[31m-=-' * 20)
print('\033[34mSequência de Fibonacci\033[m')
print('\033[31m-=-\033[m' * 20)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print('\033[31m~~~' * 20)
print('\033[33m{} -> {}'.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('\n' + '\033[31m~~~' * 20)
