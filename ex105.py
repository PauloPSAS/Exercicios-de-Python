def notas(*n, sit=False):
    """
    => Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas do aluno (aceita várias).
    :param sit: Valor opcional, indica se deve ou não mostrar a situação do aluno.
    :return: Dicionário com as informações do aluno.
    """
    mai = men = med = 0
    dic = dict()
    dic['total'] = len(n)
    for i, v in enumerate(n):
        med += v
        if i == 0:
            mai = men = v
        else:
            if v > mai:
                mai = v
            if v < men:
                men = v
    dic['maior'] = mai
    dic['menor'] = men
    dic['média'] = med / len(n)
    if sit:
        if dic['média'] < 6:
            dic['situação'] = 'RUIM'
        elif dic['média'] < 7.9:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'BOA'
    return dic


# Main
resp = notas(9, 9, 3, 8.4, sit=True)
help(notas)
print(resp)
