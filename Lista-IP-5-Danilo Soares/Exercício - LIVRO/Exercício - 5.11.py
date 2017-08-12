deposito=(float(input("Digite o valor do depósito inicial = ")))
juros=(int(input("Digite a taxa de juros = ")))

jurosfinal= juros/100

x=0
soma=0

while x <= 24:

    res= (deposito * jurosfinal) + deposito
    soma += res
    x +=1
    print ("{} mês = " .format(x),end="")
    print(soma)
  

    

