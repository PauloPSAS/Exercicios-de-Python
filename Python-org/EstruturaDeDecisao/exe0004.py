# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite apenas uma letra: "))
if letra.isnumeric() or len(letra) > 1 or letra.isspace():
    print("Apenas uma letra.")
else:
    if 'aeiou' in letra.lower():
        print(f"'{letra}' É VOGAL.")
    else:
        print(f"'{letra}' É CONSOANTE.")