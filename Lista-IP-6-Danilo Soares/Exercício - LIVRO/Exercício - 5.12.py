deposito=(float(input("Digite o valor do depósito inicial = ")))
juros=(int(input("Digite a taxa de juros = ")))
depositomensal=(float(input("Digite o valor do depositomensal = ")))

jurosfinal= juros/100

x=0


while x <= 23:

    res= (deposito * jurosfinal)
    taxa= res + deposito
    taxa += depositomensal
    deposito= taxa
    x +=1
    print ("{} mês(es) = {:.2f}" .format(x,deposito))

