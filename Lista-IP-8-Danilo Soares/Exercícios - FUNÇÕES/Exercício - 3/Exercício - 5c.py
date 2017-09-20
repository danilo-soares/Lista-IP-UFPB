import bibliotecaFly
recife=0
fortaleza=0

for i in range(10):
    destino=str(input("Destino -> "))
    turno=str(input("Turno -> "))
    valortotal=bibliotecaFly.calculaValorVoo(destino,turno)
    print("Valor da Passagem -> {}" .format(valortotal))
    if valortotal == ("Destino Inválido") or valortotal == ("Horário Inválido"):
        destino=str(input("Destino -> "))
        turno= str(input("Turno -> "))
    if destino == "recife":
        recife += valortotal
    if destino == "fortaleza":
        fortaleza += valortotal
    
