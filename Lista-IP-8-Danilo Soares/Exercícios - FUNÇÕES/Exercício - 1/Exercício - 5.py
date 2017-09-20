import bibliotecaFuction
cont=0
totaldivisores=0

for i in range(20):
    numero=int(input("Digite um número = "))

    multiplos=bibliotecaFuction.testaMultiplo4(numero)
    if multiplos == True:
        cont += 1
    divisor= bibliotecaFuction.testaDivisor(300,numero)
    if divisor == True:
        divisor = numero
    
    totaldivisores += divisor

print("{} múltiplos" .format(cont))
print("Soma dos Divisores = {}" .format(totaldivisores))
