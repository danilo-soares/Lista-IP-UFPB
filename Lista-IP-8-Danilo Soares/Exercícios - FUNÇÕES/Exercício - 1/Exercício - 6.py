import bibliotecaFuction
maior=0

for i in range(10):
    numero= int(input("Digite um número = "))

    maior= bibliotecaFuction.calculaMaior(numero,maior)

print("O maior número {} " .format(maior))
