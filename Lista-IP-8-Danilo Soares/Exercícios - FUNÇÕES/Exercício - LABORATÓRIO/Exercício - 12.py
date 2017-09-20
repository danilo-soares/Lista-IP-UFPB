import bibliotecaCorreios
custototal=0
cont=0

for i in range (8):
    tipo=(input("Tipo do Item -> "))
    peso=float(input("Peso [Em gramas] -> "))
    embalagem=(input("Embalagem -> "))
    tipoentrega=(input("Tipo Entrega -> "))
    if tipoentrega == "sedex":
        cont+=1
    custoitem= bibliotecaCorreios.calculoCustoItem(tipo,peso)
    custoembalagem=bibliotecaCorreios.calculoCustoEmbalagem(embalagem)
    custoentrega=bibliotecaCorreios.calculoCustoEntrega(tipoentrega)

    custo= custoitem+custoembalagem+custoentrega
    custototal+= custo
    
print("Valor total dos pedidos foi de {:.2f} " .format(custototal))
print("Foram {} enviados pelo SEDEX" .format(cont))
