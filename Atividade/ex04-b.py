def aplicar_prova():
  gabarito = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']
  notas = []
  continuar = 'S'

  while continuar == 'S':
    print("\n === Registro de Repostas ===")
    respostas = []
    for i in range(1, 11):
      resposta = input(f'Resposta da questão {i}: ').upper()
      respostas.append(resposta)

    acertos = sum(1 for i in range(10) if respostas[i] == gabarito[i])
    notas.append(acertos)
    print(f'Aluno teve {acertos} acertos')

    continuar = input(f'\n Outro aluno fez a prova? (S/N): ').upper()

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


aplicar_prova()