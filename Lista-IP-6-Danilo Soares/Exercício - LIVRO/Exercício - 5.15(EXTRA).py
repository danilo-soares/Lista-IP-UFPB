codigo=int(input("Código do Produto -> "))
quantidade= int(input("Quantidade Compradas -> "))
total=0

while codigo != 0:

    if codigo == 1:
        total += quantidade * 0.50
        
    elif codigo == 2:
        total += quantidade * 1
        
    elif codigo == 3:
        total += quantidade * 4
        
    elif codigo == 5:
        total += quantidade * 7
        
    elif codigo == 9:
        total += quantidade * 8
        
    else:
        print("Código Inválido")

    codigo=int(input("Código do Produto -> "))
    quantidade= int(input("Quantidade Compradas -> "))

print("Total das Compras -> {:.2f}" .format(total))
