palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso',
            'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado',
            'Programador', 'Futuro')
for p in palavras:
    print(f'\nNa palavra "{p.upper()}" temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
