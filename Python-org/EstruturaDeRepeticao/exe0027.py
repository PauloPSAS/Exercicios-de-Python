"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""


def media_turmas(q):
    m = 0
    for turma in q:
        m += turma
    m /= len(q)
    return m


def turmas(qtd):
    alunosPorTurma = []
    for turma in range(1, qtd + 1):
        while True:
            print(f"\nQuantos alunos têm na {turma}ª turma? ", end='')
            a = int(input())
            if a <= 0 or a > 40:
                print("\nA turma têm que ter entre 1 e 40 alunos apenas...")
            else:
                alunosPorTurma.append(a)
                break
    return alunosPorTurma


qtdTurmas = int(input("Quantas Turmas são: "))
qtdAlunosTurma = turmas(qtdTurmas)
media = media_turmas(qtdAlunosTurma)

print(f"\nSão {qtdTurmas} Turmas.")
for a in range(1, qtdTurmas + 1):
    print(f"{a}ª Turma: {qtdAlunosTurma[a-1]} alunos.")
print(f"A média de alunos por turma é de: {media:.1f} alunos.")
