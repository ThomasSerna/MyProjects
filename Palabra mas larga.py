#           Notas
#Este programa obtiene la frase que tu le des y este busca la palabra mas larga y cuantas letras tiene.

txt = str(input('Dame una frase para encontrar la palabra mas larga: '))
x = txt.split()
n = 0
for i in x:
    if len(i) > n:
        n = len(i)
        n1 = i
print(f'\nLa palabra mas larga en este string es "{n1}" con {len(n1)} letras')