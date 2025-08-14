def calcMedia(n1, n2):
    media = (n1 + n2) / 2
    return media

n1 = 5
n2 = 8

media = calcMedia(n1, n2)

if media >= 9:
    print(f'nota 1: {n1}, nota 2: {n2}, media: {media}, conceito: A | {'Aprovado'}')
elif media >= 7.5:
    print(f'nota 1: {n1}, nota 2: {n2}, media: {media}, conceito: B | {'Aprovado'}')
elif media >= 6:
    print(f'nota 1: {n1}, nota 2: {n2}, media: {media}, conceito: C | {'Aprovado'}')
elif media >= 4:
    print(f'nota 1: {n1}, nota 2: {n2}, media: {media}, conceito: D | {'Reprovado'}')
else:
    print(f'nota 1: {n1}, nota 2: {n2}, media: {media}, conceito: E | {'Reprovado'}')