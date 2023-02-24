from random import randint
vel = randint(10, 180)
print('\n')
print('-=-' * 25)
print('Então estava à {:.1f}Km/h?'.format(vel))
if vel > 80:
    multa = 7 * (vel - 80)
    dif = vel - 80
    print('O dono do veículo deve pagar R${:.2f} de multa por dirigir à {:.1f}Km/h. {}Km Acima do permitido.'.format(multa, vel, dif))
else:
    dif = 80 - vel
    print('O veículo está a {}Km abaixo do limite permitido'.format(dif))
print('-=-' * 25)
print('\nDirija com cuidado.')
print('    ---FIM---')
