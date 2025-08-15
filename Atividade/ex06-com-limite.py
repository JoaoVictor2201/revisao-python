"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
• Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
• Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
• A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

while True:
    anoContratado = int(input("Em que ano você foi contratado? "))
    anoAtual = 2025
    porcentagemInicial = 1.5
    porcentagemFinal = 0
    if anoContratado < 1995:
        print("O ano de contratação deve ser posterior a 1995.")
    salarioInicial = float(input("Qual era o seu salário inicial? "))
    try:
        if salarioInicial <= 0:
            print("Salário inicial deve ser maior que zero.")
            continue
    except ValueError:
        print("Salário inválido.")
    calculo = anoContratado - anoAtual
    while porcentagemFinal <= 30:
        pass
     
        
