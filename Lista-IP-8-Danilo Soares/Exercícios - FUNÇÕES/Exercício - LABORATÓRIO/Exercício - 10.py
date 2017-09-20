import bibliotecaCorreios

tipo=(input("Tipo do Item -> "))
peso=float(input("Peso [Em gramas] -> "))
embalagem=(input("Embalagem -> "))
tipoentrega=(input("Tipo Entrega -> "))

custoitem= bibliotecaCorreios.calculoCustoItem(tipo,peso)
custoembalagem=bibliotecaCorreios.calculoCustoEmbalagem(embalagem)
custoentrega=bibliotecaCorreios.calculoCustoEntrega(tipoentrega)

custototal= custoitem+custoembalagem+custoentrega

print(custototal)
