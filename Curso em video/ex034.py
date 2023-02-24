salario = float(input('Qual é o salário do funcionário? '))
if salario >= 1250.0:
    aumento = salario + (10 * salario / 100)
else:
    aumento = salario + (15 * salario / 100)
print('Se o salário é R${:.2f} agora passará a receber R${:.2f}.'.format(salario, aumento))
