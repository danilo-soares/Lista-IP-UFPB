import bibliotecaCorreios
custototal=0

for i in range (2):
    tipo=(input("Tipo do Item -> "))
    peso=float(input("Peso [Em gramas] -> "))
    embalagem=(input("Embalagem -> "))
    tipoentrega=(input("Tipo Entrega -> "))

    custoitem= bibliotecaCorreios.calculoCustoItem(tipo,peso)
    custoembalagem=bibliotecaCorreios.calculoCustoEmbalagem(embalagem)
    custoentrega=bibliotecaCorreios.calculoCustoEntrega(tipoentrega)
    custo= custoitem + custoembalagem + custoentrega
    custototal += custo

print("R$ {:.2f}" .format(custototal))
