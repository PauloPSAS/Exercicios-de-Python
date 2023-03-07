"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;"""

print("{:^40}".format('LADOS DE UM TRIÂNGULO'))
l1 = int(input("Digite um o tamanho de um lado  do triângulo: "))
l2 = int(input("Digite outro lado do triângulo: "))
l3 = int(input("Digite o último lado do triângulo: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("FORMA UM TRIÂNGULO")
    print("Tipo: ", end='')
    if l1 == l2 == l3 == l1:
        print("EQUILÁTERO.")
    elif l1 != l2 != l3 != l1:
        print("ESCALENO.")
    else:
        print("ISÓSCELES.")

else:
    print("NÃO FORMA UM TRIÂNGULO")
