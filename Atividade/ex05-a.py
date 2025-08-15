"""
5. O cardápio de uma lanchonete é o seguinte:

Especificação Código Preço
Cachorro Quente 100 R$ 1,20
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20
Cheeseburguer 104 R$ 1,30
Refrigerante 105 R$ 1,00


Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 

Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.

Considere que o cliente deve informar quando o pedido deve ser encerrado.

"""

cardapio = {
  100:['Cachorro Quente', 1.20],
  101:['Bauru Simples', 1.30],
  102: ['Bauru com ovo', 1.50],
  103: ['Hambúrguer', 1.20],
  104: ['Cheeseburguer', 1.30],
  105: ['Refrigerante', 1.00]
}

conta = 0

print('Menu de hoje')
for codigo, (nome, preco) in cardapio.items():
    print(f'{codigo} | {nome}: {preco}')

while True:
    opcaoClienteCodigo = int(input("Digite o códgio do produto (0 para encerrar): "))
    if opcaoClienteCodigo == 0:
        break
    if opcaoClienteCodigo not in cardapio:
        print("Código inválido")
        continue
    opcaoClienteQuantidade = int(input("Digite a quantidade: "))

    nome, preco = cardapio[opcaoClienteCodigo]
    valorItem = preco * opcaoClienteQuantidade
    conta += valorItem
    print(valorItem)
print(conta)
