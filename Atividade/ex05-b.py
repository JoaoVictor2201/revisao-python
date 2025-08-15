cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

print("==== Cardápio ====")
for codigo, (nome, preco) in cardapio.items():
    print(f"{codigo} - {nome:<15} R$ {preco:.2f}")

conta = 0

while True:
    try:
        codigo = int(input("\nDigite o código do item (ou 0 para encerrar): "))

        if codigo == 0:
            break
        
        if codigo in cardapio:
            qtd = int(input('Quantidade: '))
            nome, preco = cardapio[codigo]
            total = preco * qtd
            conta += total
            print(f"{qtd} x {nome} = R$ {total:.2f}")
        else:
            print("Código inválido. Tente novamente.")

    except ValueError:
        print("Entrada inválida")

print(f'Valor da conta: {conta}')
    