preco = 399
notas = [100, 50, 10, 5, 1]

print(f'{preco}')
for nota in notas:
    qtdNotas = preco // nota
    preco -= qtdNotas * nota
    print(f'{qtdNotas} nota(s) de R$ {nota},00')