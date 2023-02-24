from random import choice
a1 = str(input('Nome do primeiro aluno escolhido: '))
a2 = str(input('Nome do segundo aluno escolhido: '))
a3 = str(input('Nome do terceiro aluno escolhido: '))
a4 = str(input('Nome do quarto aluno escolhido: '))
lista = [a1, a2, a3, a4]
sortudo = choice(lista)
print('O Sortudo foi: ', sortudo)
