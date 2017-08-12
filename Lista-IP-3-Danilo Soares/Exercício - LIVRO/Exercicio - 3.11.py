							##Exercício - 3.11
valorproduto=(float(input("Digite o valor do produto = ")))
desconto=(float(input("Digite o percentual de desconto = ")))

desconto=(desconto/100)
valor_final=( valorproduto - (desconto * valorproduto))

print("O valor com desconto é {}" .format(valor_final))
