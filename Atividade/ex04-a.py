gabarito = ["B", "D", "D", "A", "B", "C", "D", "B", "E", "C"]

def coletar_respostas():
    respostas = []
    for i in range(1, 11):
        while True:
            resp = input(f"ALTERNATIVA DA PERGUNTA {i}: ").strip().upper()
            if resp in ["A", "B", "C", "D", "E"]:
                respostas.append(resp)
                break
            else:
                print("Resposta inválida. Digite apenas A, B, C, D ou E.")
    return respostas

notas = []

def comparar_respostas(respostas):
    pontos = 0
    for i in range(len(gabarito)):
        if respostas[i] == gabarito[i]:
            pontos += 1
    notas.append(pontos)
    print(f"Sua nota foi {pontos}")

def mostrar_notas():
    if notas:
        maior = max(notas)
        menor = min(notas)
        total_alunos = len(notas)
        media = sum(notas) / total_alunos

        print("\n=== Resultados Finais ===")
        print(f"Maior número de acertos: {maior}")
        print(f"Menor número de acertos: {menor}")
        print(f"Total de alunos: {total_alunos}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhum aluno respondeu a prova.")

while True:
    respostas_aluno = coletar_respostas()
    comparar_respostas(respostas_aluno)
    continuar = input("Outro aluno deseja fazer a prova? (sim/não): ").strip().lower()
    if continuar != "sim":
        break

mostrar_notas()
