def calculoPreco(tipo, qtdLitros):
    precoAlcool = 1.90
    precoGasolina = 2.50
    valorTotal = 0
    
    if tipo == "G":
        if qtdLitros <= 20:
            valorTotal = (precoGasolina * qtdLitros)
            valorDesconto = valorTotal - (valorTotal * 0.04)
            return valorDesconto
        else:
            valorTotal = (precoGasolina * qtdLitros)
            valorDesconto = valorTotal - (valorTotal * 0.06)
            return valorDesconto
    elif tipo == "A":
        if qtdLitros <= 20:
            valorTotal = (precoAlcool * qtdLitros)
            valorDesconto = valorTotal - (valorTotal * 0.03)
            return valorDesconto 
        else:
            valorTotal = (precoAlcool * qtdLitros)
            valorDesconto = valorTotal - (valorTotal * 0.05)
            return valorDesconto


print(calculoPreco("G", 19))
print(calculoPreco("G", 21))

print(calculoPreco("A", 19))
print(calculoPreco("A", 21))