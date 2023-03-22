"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""


login = str(input("Nome de usuário: "))
while True:
    senha = str(input("Senha: "))
    if senha == login:
        print("\nSenha Igual ao login, digite outra senha: ", end='')
    else:
        break
print()
print("Login: {}".format(login))
print("Senha: {}".format(senha))
