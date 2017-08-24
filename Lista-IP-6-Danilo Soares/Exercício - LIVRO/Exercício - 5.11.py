deposito=(float(input("Digite o valor do depósito inicial = ")))
juros=(float(input("Digite a taxa de juros = ")))
jurospg=0

jurosfinal= juros/100

x=0

while x < 24:

    taxa= (deposito * jurosfinal)
    taxafinal= taxa + deposito
    deposito = taxafinal
    jurospg += taxa
    x += 1
    print("{} mês = R$ {:.2f}" .format(x,taxafinal))
    
print("Você pagou R$ {:.2f} de acréscimo" .format(jurospg))

    

