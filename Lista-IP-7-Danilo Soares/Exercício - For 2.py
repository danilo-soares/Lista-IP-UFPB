quantidade=int(input("Digite a quantidade lavagens = "))
valor=[]
res=0
cont=0
total=0

for i in range(quantidade):

    tipocobra=str.lower(input("Digite o tipo de cobrança = "))
     
    if tipocobra == "peça":
        quantidade=int(input("Digite a quantidade de peças = "))
        lavagem= str.lower(input("Lavagem a seco [S/N] ? "))
        cont = quantidade * 7 
        if lavagem == "s":    
            res = 1
            cont += 3.5
        valor.append(cont)

    elif tipocobra == "peso":
        quilos= int(input("Digite a quantidade de quilos = "))
        lavagem= str.lower(input("Lavagem a seco [S/N] ? "))
        cont= quilos * 5
    
        if lavagem == "s":    
            res = 1
            cont += 3.5
        valor.append(cont)
    total+=cont
numero=1

for i in valor[::1]:
    print("Valor do {}º pedido = " .format(numero), end="")
    print(i)
    numero += 1
print("Total arrecadado -> R$ {:.2f} " .format(total))
print("Quantidade de lavagens a seco -> {} " .format(res))
