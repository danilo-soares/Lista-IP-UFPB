import bibli3

nome=input("Nome do Prédio -> ")
dias=int(input("Dias de Atraso -> "))

total= bibli3.calculaCondominio(nome,dias)

print("Você Pagará {:.2f}" .format(total))
