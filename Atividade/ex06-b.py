salarioInicial = 1000
salarioAtual = salarioInicial

anoInicio = 1995
anoAtual = 2025
percAumento = 1.5

for ano in range(anoInicio + 1, anoAtual + 1):
  aumento = salarioAtual * (percAumento / 100)
  salarioAtual += aumento
  print(f'Ano {ano} - Aumento: {percAumento:.2f}% - Salario: R$ {salarioAtual:.2f}')
  percAumento += 2

print(f'\n Salario atual em {anoAtual}: R$ {salarioAtual:.2f}')