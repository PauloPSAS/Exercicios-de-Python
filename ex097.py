def escreva(msg):
    t = len(msg) + 4
    print('\033[1;33m~\033[m' * t)
    print(f'\033[36m  {msg}')
    print('\033[1;33m~\033[m' * t)


# Main
escreva('Paulo Souza')
escreva('Curso de Python no YouTube')
escreva('CeV')
