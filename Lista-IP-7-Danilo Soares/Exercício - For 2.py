quantidade=int(input("Digite a quantidade lavagens = "))
tipocobra=str.lower(input("Digite o tipo de cobrança = "))
res=0
cont=0

for i in range(quantidade):

    if tipocobra == "peça":
        quantidade=int(input("Digite a quantidade de peças = "))
        cont = quantidade * 7 

    elif tipocobra == "peso":
        quilos= int(input("Digite a quantidade de quilos = "))
        cont= quilos * 5

    lavagem= str.lower(input("Lavagem a seco [S/N] ? "))
    tipocobra=str.lower(input("Digite o tipo de cobrança = "))

    if lavagem == "s":
        res = 1
        cont += 3.5
    
print("Valor do pedido -> R$ {} " .format(cont))
print("Total arrecadado -> R$ {} " .format(cont))
print("Quantidade de lavagens a seco -> {} " .format(res))
