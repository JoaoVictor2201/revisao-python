gabarito = ["B", "D", "D", "A", "B", "C", "D", "B", "E", "C"]

def respostas(respostas=""): 
    totalPerguntas = 0  
    questão = 1
    respostas = []
    while totalPerguntas < 10:  
        respostaAluno = input(f"ALTERNATIVA DA PERGUNTA {questão}: ")
        if respostaAluno == "A" or respostaAluno == "B" or respostaAluno == "C" or respostaAluno == "D" or respostaAluno == "E":
            questão += 1
            respostas.append(respostaAluno)
            totalPerguntas += 1
    return respostas 

notas = []
def comparador(respostas):
    numAlunos = 1
    global pontos
    pontos = 0
    for i in range(len(respostas)):
        if respostas[i] == gabarito[i]:
            pontos += 1
        notas.append[pontos]
    print(f"sua nota foi {pontos}")

    aluno = input("outro aluno deseja fazer a prova? ")
    if aluno == "sim" or aluno == "SIM":
        numAlunos += 1
        return True
    return numAlunos

def mostrarNotas(notas):
    if notas:
        maior = max(notas)
        menor = min(notas)
        totalAlunos = len(notas)
        media = sum(notas) / totalAlunos

        print("\n=== Resultados Finais ===")
        print(f"Maior número de acertos: {maior}")
        print(f"Menor número de acertos: {menor}")
        print(f"Total de alunos: {totalAlunos}")
        print(f"Média da turma: {media:.2f}")

    else:
        print("Nenhum aluno respondeu a prova.")

while True:
    lista_respostas = respostas()
    repetir = comparador(lista_respostas)
    mostrar = mostrarNotas(notas)
    break