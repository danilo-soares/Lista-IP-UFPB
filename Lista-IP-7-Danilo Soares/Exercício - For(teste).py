quantidade=int(input("Digite a quantidade lavagens = "))
res=0
cont=0
total=0

for i in list(range(quantidade)):

    tipocobra=str.lower(input("Digite o tipo de cobrança = "))

    if tipocobra == "peça":
        quantidade=int(input("Digite a quantidade de peças = "))
        cont = quantidade * 7 
        valor = cont

    elif tipocobra == "peso":
        quilos= int(input("Digite a quantidade de quilos = "))
        cont = quilos * 5
        valor=cont

    lavagem= str.lower(input("Lavagem a seco [S/N] ? "))
    
    if lavagem == "s":
        res = 1
        cont += 3.5

    total += cont

if quantidade > 1:

    for valor in [valor]:
        print ("Valor do pedido -> {} " .format(valor))

else:

    print("Valor do pedido -> {} " .format(valor))

print("Total arrecadado -> R$ {} " .format(total))
print("Quantidade de lavagens a seco -> {} " .format(res))

