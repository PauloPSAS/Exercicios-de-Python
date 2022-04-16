from math import sin, cos, tan, radians
x = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(x, sin(radians(x))))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'. format(x, cos(radians(x))))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(x, tan(radians(x))))
