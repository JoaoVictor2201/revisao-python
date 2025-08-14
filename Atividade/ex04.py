gabarito = ["B", "D", "D", "A", "B", "C", "D", "B", "E", "C"]

def respostas(respostas=""): 
    maximo = 0  
    numeroAlternativa = 1
    respostas = []
    while maximo < 10:  
        opcao = input(f"ALTERNATIVA DA PERGUNTA {numeroAlternativa}: ")
        if opcao == "A" or opcao == "B" or opcao == "C" or opcao == "D" or opcao == "E":
            numeroAlternativa += 1
            respostas.append(opcao)
            maximo += 1
    return respostas 

def comparador(respostas):
    pontos = 0
    for i in range(len(respostas)):
        if respostas[i] == gabarito[i]:
            pontos += 1
    print(f"sua nota foi {pontos}")

    aluno = input("outro aluno deseja fazer a prova? ")
    if aluno == "sim" or aluno == "SIM":
        return True
    return False

alunos = []
notas = []

while True:
    lista_respostas = respostas()
    repetir = comparador(lista_respostas)
    if not repetir:
        break
