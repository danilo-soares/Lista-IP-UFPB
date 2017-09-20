import bibliotecaFly

destino=str(input("Destino -> "))
turno=str(input("Turno -> "))

valortotal= bibliotecaFly.calculaValorVoo(destino,turno)

print("Valor da Passagem -> {}" .format(valortotal))
